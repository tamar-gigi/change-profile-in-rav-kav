import cv2
from myProject.getLocation.getLocation import getLocationText
import os
from PIL import Image
from myProject.reSize.reSizeImage import resizeWithWhiteBackground as reSize
from numpy import argmax
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from myProject.removeLine.remove_lines import removeLines


def cropLetters(image, loc, index, model):
    ind = 0
    # save the location word
    for location in loc:
        (x, y, w, h) = location
        imgC = image[y:y + h, x:x + w]
        cv2.imwrite(fr'myProject/cropLocation/imgCrop/imgC{index}/i{ind}.png', imgC)

        ind += 1
    indexWord = 0
    wordStr = ''
    arrayWords = []
    # crop word to letters
    for img in sorted(os.listdir(fr'myProject/cropLocation/imgCrop/imgC{index}')):
        # open image word
        with Image.open(fr'myProject/cropLocation/imgCrop/imgC{index}/{img}') as imgC:
            (width, height) = imgC.size
            # when the image word biggest or smallest- return
            if width > 200 or height > 200 or width < 5 or height < 5:
                continue
            countWhite = [0] * width
            # count how many white pixels there are in each column
            for row in range(height):
                for col in range(width):
                    color = imgC.getpixel((col, row))
                    if color == 255:
                        countWhite[col] += 1
            start, end = 0, 0
            # crop letters
            for col in range(0, width - 1, 1):
                if countWhite[col] != countWhite[col + 1] or (
                        (col == 0 or col == width - 2) and countWhite[col] != height):
                    if countWhite[col] == height or col == 0:
                        start = col + 1
                    if countWhite[col + 1] == height or col == width - 2:
                        end = col + 1
                    # found letter- crop, save, send to predict model
                    if end and start:
                        imageCrop = imgC.crop((int(start - 1), 0, int(end), int(height)))
                        path = fr'myProject/cropLocation/imgCrop/imgL{index}/letter{indexWord}.png'
                        imageCrop.save(f'{path}', format="png")
                        indexWord += 1
                        reSize(f'{path}', f'{path}', 28)
                        char = myModel(path, model)
                        if char.isdigit():
                            wordStr += char
                        else:
                            wordStr = char + wordStr
                        start, end = 0, 0
        arrayWords.append(wordStr)
        wordStr = ''
    print(index, arrayWords)
    return arrayWords


def myModel(path, model):
    # load the image
    img = load_img(path, color_mode="grayscale", target_size=(28, 28))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 1 channel
    img = img.reshape(1, 28, 28, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    # predict the class
    predict_value = model.predict(img)
    digit = argmax(predict_value)
    return convertDigit(digit)


def convertDigit(digit):
    # convert the index that get in predict model to letter
    arrClass = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '-', '.', '/', ':', 'א', 'ב', 'ג', 'ד', 'ה', 'ו',
                'ז', 'ח', 'ט', 'י', 'ך', 'כ', 'ל', 'ם', 'מ', 'ן', 'נ', 'ס', 'ע', 'ף', 'פ', 'ץ', 'צ', 'ק', 'ר', 'ש', 'ת']
    return arrClass[int(digit)]


def my_func(i_file, place, black, index, arrResult):
    # load model
    model = load_model(fr'myProject/model/model_alpha_beta_tubs.h5')
    # remove lines- when the file is student permit
    if index == 1:
        removeLines(f'{i_file}')
    # load image
    image = cv2.imread(i_file, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (image.shape[1] // place, image.shape[0] // place))
    (thresh, image) = cv2.threshold(image, black, 255, cv2.THRESH_BINARY)
    # get location words form files
    loc = getLocationText(image)
    # crop letter location and predict in the model
    arrResult[index] = cropLetters(image, loc, index, model)


def startRun(files):
    size = [4, 2, 4, 6]
    black = [68, 52, 55, 85]

    import multiprocessing
    with multiprocessing.Manager() as manager:
        listText = manager.list()
        listText.append([])
        listText.append([])
        listText.append([])
        listText.append([])
        p_arr = []
        for index, i_file in enumerate(files):
            p = multiprocessing.Process(target=my_func, args=(i_file, size[index], black[index], index, listText))
            p_arr.append(p)
        for p in p_arr:
            p.start()
        for p in p_arr:
            p.join()
        return list(listText)


if __name__ == '__main__':
    s=startRun(['../camScanner/img/t_id.jpg', '../camScanner/img/t_aos.jpg', '../camScanner/img/t_s.jpg',
              '../camScanner/img/t_r.jpg'])
    for di in os.listdir(f'../cropLocation/imgCrop'):
        for deli in os.listdir(f'../cropLocation/imgCrop/{di}'):
            if os.path.isfile(f'../cropLocation/imgCrop/{di}/{deli}'):
                os.remove(f'../cropLocation/imgCrop/{di}/{deli}')
