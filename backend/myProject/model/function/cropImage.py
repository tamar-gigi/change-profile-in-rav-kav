from PIL import Image
from reSizeImage import resizeWithWhiteBackground
from pdf2image import convert_from_path


def cropRow(image):
    w, h = image.size
    countWhiteRow = [0]*h
    for i in range(w):
        for j in range(h):
            color = image.getpixel((i, j))
            color = (color[0]+color[1]+color[2])/3
            if color == 255:
                countWhiteRow[j] += 1
    start, end = 0, 0
    locationRows = []
    for i in range(h - 1):
        if countWhiteRow[i] != countWhiteRow[i + 1]:
            if countWhiteRow[i] == w:
                start = i + 1
            if countWhiteRow[i + 1] == w:
                end = i + 1
            if end != 0 and start != 0 and end - start > 2:
                box = [0, start, w - 1, end]
                locationRows.append(box)
                end, start = 0, 0

    return locationRows


def cropLetters(image, locRow, path1):
    w, h = image.size
    countWhiteCol = [0]*w
    index=1
    start, end = 0, 0
    locationLetters = []
    cropLetters = []
    for loc in locRow:
        hight = int(loc[3]) - int(loc[1])
        for i in range(w):
            for j in range(loc[1], loc[1]+hight):
                color = image.getpixel((i, j))
                color = (color[0] + color[1] + color[2] ) / 3
                if color == 255:
                    countWhiteCol[i] += 1
        for row in range(w - 1):
            if countWhiteCol[row] != countWhiteCol[row + 1]:
                if countWhiteCol[row] == hight:
                    start = row+1
                if countWhiteCol[row + 1] == hight:
                    end = row+1
                if end != 0 and start != 0 and end - start > 2:
                    box = [start, loc[1], end, loc[3]]
                    locationLetters.append(box)
                    imageCrop = image.crop(box)
                    cropLetters.append(imageCrop)
                    path = fr'../{path1}/{index}.png'
                    imageCrop.save(path)
                    resizeWithWhiteBackground(fr'{path1}/{index}.png', fr'{path1}/{index}.png', 60)
                    index += 1

                    end, start = 0, 0
        countWhiteCol = [0] * w


if __name__ == '__main__':
    # poppler_path = r'C:\Users\User\Downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'
    # pages = convert_from_path(pdf_path=f'../myProject/images/all/alfaBeta.pdf', dpi=500,
    #                           poppler_path=poppler_path)
    # for page in pages:
    #     path = f'../myProject/images/alfaBeta.png'
    #     page.save(path, 'PNG')

    image = Image.open(f'../myProject/images/all/alfaBeta.png')
    locRow = cropRow(image)
    cropLetters(image, locRow, f'myProject/images/all')
