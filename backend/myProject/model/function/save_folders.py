from sklearn.model_selection import train_test_split
import os
import shutil
from PIL import Image
import numpy as np


def saveTrainTestValidate(pathImage, newPathImageTest, newPathImageTrain, newPathImageValidate):
    X = []
    baseDir = fr'../{pathImage}'
    for i in sorted(os.listdir(baseDir)):
        for j in sorted(os.listdir(fr'{baseDir}/{i}')):
            X.append(j)

        # division for train and test
        dirTrainValidate, dirTest = train_test_split(X, test_size=0.2, random_state=42)

        c = 1
        for item in dirTest:
            ori = fr'{baseDir}/{i}/{item}'
            dest = fr'../{newPathImageTest}/{i}/{c}.png'
            shutil.copy(ori, dest)
            c += 1

        # division for train and validate
        dirTrain, dirValidate = train_test_split(dirTrainValidate, test_size=0.1, random_state=42)

        c = 0
        for item in dirTrain:
            ori = fr'{baseDir}/{i}/{item}'
            dest = fr'../{newPathImageTrain}/{i}/{c}.png'
            shutil.copy(ori, dest)
            c += 1

        c = 0
        for item in dirValidate:
            ori = fr'{baseDir}/{i}/{item}'
            dest = fr'../{newPathImageValidate}/{i}/{c}.png'
            shutil.copy(ori, dest)
            c += 1
        X = []


def arrayNumpyTrainTestValidate(pathImage):
    X = []
    Y = []
    index = 0
    baseDir = fr'../{pathImage}'
    for i in sorted(os.listdir(baseDir)):
        for j in sorted(os.listdir(fr'{baseDir}/{i}')):
            imgOpen=Image.open(fr'{baseDir}/{i}/{j}')
            imgArray=np.array(imgOpen)
            X.append(imgArray)
            Y.append([index])
        index += 1
    X=np.array(X)
    Y=np.array(Y)
    XTrainValidate, XTest, YTrainValidate, YTest = train_test_split(X, Y, test_size=0.2, random_state=42)

    XTrain, XValidate, YTrain, YValidate = train_test_split(XTrainValidate, YTrainValidate, test_size=0.1, random_state=42)

    return XTrain, YTrain, XTest, YTest, XValidate, YValidate


def trainTest(testPath, trainPath):
    XTrain = []
    YTrain = []
    indexTrain = 0
    for dir in sorted(os.listdir(fr'../{trainPath}')):
        for item in sorted(os.listdir(fr'../{trainPath}/{dir}')):
            imageOpen = Image.open(fr'../{trainPath}/{dir}/{item}')
            imageGray = imageOpen.convert('L')
            imageArr = np.array(imageGray)
            XTrain.append(imageArr)
            YTrain.append([indexTrain])
        indexTrain += 1
    XTrain = np.array(XTrain)
    YTrain = np.array(YTrain)

    XTest = []
    YTest = []
    indexTest = 0
    for dir in sorted(os.listdir(fr'../{testPath}')):
        for item in sorted(os.listdir(fr'../{testPath}/{dir}')):
            imageOpen = Image.open(fr'../{testPath}/{dir}/{item}')
            imageGray = imageOpen.convert('L')
            imageArr = np.array(imageGray)
            XTest.append(imageArr)
            YTest.append([indexTest])
        indexTest += 1
    XTest = np.array(XTest)
    YTest = np.array(YTest)
    return XTrain, YTrain, XTest, YTest


def trainTestNumber(pathImage):
    X = []
    Y = []
    index = 0
    baseDir = fr'../{pathImage}'
    for i in sorted(os.listdir(baseDir)):
        for j in sorted(os.listdir(fr'{baseDir}/{i}')):
            imgOpen=Image.open(fr'{baseDir}/{i}/{j}')
            imgGray = imgOpen.convert('L')
            imgArray=np.array(imgGray)
            X.append(imgArray)
            Y.append([index])
        index += 1
    X=np.array(X)
    Y=np.array(Y)
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.2, random_state=42)


    return XTrain, YTrain, XTest, YTest


def saveTrainTestValidate1(pathImage, newPathImageTest, newPathImageTrain, newPathImageValidate):
    X = []
    baseDir = fr'{pathImage}'
    for i in sorted(os.listdir(baseDir)):
        for j in sorted(os.listdir(fr'{baseDir}/{i}')):
            X.append(j)

        # division for train and test
        dirTrainValidate, dirTest = train_test_split(X, test_size=0.2, random_state=42)

        c = 1
        os.mkdir(fr'{newPathImageTest}/{i}')
        for item in dirTest:
            ori = fr'{baseDir}/{i}/{item}'
            dest = fr'{newPathImageTest}/{i}/{c}.png'
            shutil.copy(ori, dest)
            c += 1

        # division for train and validate
        dirTrain, dirValidate = train_test_split(dirTrainValidate, test_size=0.1, random_state=42)

        c = 0
        os.mkdir(fr'{newPathImageTrain}/{i}')
        for item in dirTrain:
            ori = fr'{baseDir}/{i}/{item}'
            dest = fr'{newPathImageTrain}/{i}/{c}.png'
            shutil.copy(ori, dest)
            c += 1

        c = 0
        os.mkdir(fr'{newPathImageValidate}/{i}')
        for item in dirValidate:
            ori = fr'{baseDir}/{i}/{item}'
            dest = fr'{newPathImageValidate}/{i}/{c}.png'
            shutil.copy(ori, dest)
            c += 1
        X = []
