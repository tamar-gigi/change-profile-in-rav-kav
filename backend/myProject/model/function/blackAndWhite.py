import os
from PIL import Image


def blackAndWhite(path,newPath):
    # running on the photos
    for dirLetters in os.listdir(fr'../{path}'):
        for image in os.listdir(fr'../{path}/{dirLetters}'):
            imageOrginul = Image.open(fr'../{path}/{dirLetters}/{image}')

            # image height and width
            w, h = imageOrginul.size
            for i in range(h):
                for j in range(w):
                    # pixel color
                    r, g, b = imageOrginul.getpixel((i, j))
                    # if larger than 200 paint in white
                    if (r+g+b) / 3 >= 200:
                        imageOrginul.putpixel((i, j), (255, 255, 255))
                    # if not paint in black
                    else:
                        imageOrginul.putpixel((i, j), (0, 0, 0))
            imageOrginul.save(fr'../{newPath}/{dirLetters}/{image}')



