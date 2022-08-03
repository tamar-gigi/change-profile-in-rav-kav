import numpy as np
from keras_preprocessing.image import ImageDataGenerator
from PIL import Image
from skimage import io
from pathlib import Path
import os


def imageGenerator(path,num):
    # defining the changes for condensation
    imageGen = ImageDataGenerator(
        zoom_range=[0.9, 1.1],
        fill_mode='reflect',
        shear_range=0.15,
        width_shift_range=0.1,
        height_shift_range=0.1
    )
    imagePath = fr'../{path}'
    myFile = Path(imagePath)
    if myFile.is_file():
        print('ok')
    else:
        print('no image')
    image = np.expand_dims(io.imread(imagePath), 0)
    augIter = imageGen.flow(image)
    augImage = [next(augIter)[0].astype(np.uint8) for i in range(num)]
    return augImage


def saveImage(images, numOfImages, path):
    index = 1
    for n in range(numOfImages):
        data = Image.fromarray(images[n])
        nameImage = fr'../{path}{index}.png'

        data.save(nameImage)
        index += 1


if __name__ == '__main__':

    import cv2
    from myProject.reSize.reSizeImage import resizeWithWhiteBackground

    s = imageGenerator(f'zzzzzzzzz/m.png', 40)
    saveImage(s, 40, f'zzzzzzzzz/m.png')
    for image in os.listdir(f'../zzzzzzzzz'):
        resizeWithWhiteBackground(fr'../zzzzzzzzz/{image}', fr'../zzzzzzzzz/{image}', 28)
        im = cv2.imread(fr'../zzzzzzzzz/{image}', cv2.IMREAD_GRAYSCALE)
        (thresh, im) = cv2.threshold(im, 80, 255, cv2.THRESH_BINARY)
        cv2.imwrite(fr'../zzzzzzzzz/{image}', im)


