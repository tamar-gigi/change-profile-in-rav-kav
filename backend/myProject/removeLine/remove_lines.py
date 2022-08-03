import cv2


def removeLines(pathImage):
    # open image
    image = cv2.imread(f'{pathImage}')
    # convert black and white color image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # found lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
    detected_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    # found contours
    contours = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    # draw lines
    for c in contours:
        cv2.drawContours(image, [c], -1, (int(image[10][10][0]), int(image[10][10][1]), int(image[10][10][2])), 2)
    repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 2))
    # result- image without lines
    result = 255 - cv2.morphologyEx(255 - image, cv2.MORPH_CLOSE, repair_kernel, iterations=1)
    # save rhe result
    cv2.imwrite(f'{pathImage}', result)
    cv2.destroyAllWindows()

