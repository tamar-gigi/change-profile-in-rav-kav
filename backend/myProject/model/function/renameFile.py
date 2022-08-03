import os


def changeNameFile(path):
    for dirLetters in os.listdir(fr'../{path}'):
        i = 1
        for image in os.listdir(fr'../{path}/{dirLetters}'):
            imageEnd = '.png'
            imageName = 'image'+str(i)
            newName = fr'{imageName}{imageEnd}'
            os.renames(fr'../{path}/{dirLetters}/{image}',
                       fr'../{path}/{dirLetters}/{newName}')
            i += 1


def changeNameFile1(path, i):
    imageEnd = '.png'
    imageName = 'image' + str(i)
    newName = fr'{imageName}{imageEnd}'
    os.renames(fr'../{path}', fr'../{path}')
