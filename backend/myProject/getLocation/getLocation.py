import pytesseract
from pytesseract import Output
import cv2


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


def getLocationText(img):
    text_pos_list = []
    # send the image to the function that return a location
    custom_config = r'-l heb --psm 6'
    d = pytesseract.image_to_data(img, output_type=Output.DICT, config=custom_config)
    n_boxes = len(d['level'])
    # loop for enter form the array location right
    for i in range(n_boxes):
        text = d['text'][i].strip()
        if len(text) == 0:
            continue
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        text_pos_list.append((x, y, w, h))
    return text_pos_list


if __name__ == '__main__':

    IMAGE_PATH = '../camScanner/img/t_aos.jpg'
    im1 = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    t = getLocationText(im1, 3)
