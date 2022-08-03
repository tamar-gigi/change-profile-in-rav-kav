# *******************************
from keras.models import load_model
from PIL import Image
from skimage import transform
import os
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import itertools


def convertDigit(digit):
    arrClass = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '-', '.', '/', ':', 'א', 'ב', 'ג', 'ד', 'ה', 'ו',
                'ז', 'ח', 'ט', 'י', 'ך', 'כ', 'ל', 'ם', 'מ', 'ן', 'נ', 'ס', 'ע', 'ף', 'פ', 'ץ', 'צ', 'ק', 'ר', 'ש', 'ת']
    return arrClass[int(digit)]


def To_classify(path):
    img = Image.open(str(path))
    img = np.array(img).astype('float32')
    img = transform.resize(img, ( 28, 28, 1))
    img = np.expand_dims(img, axis=0)
    my_model = load_model("alpha-beta-tubs-model.h5")
    output = my_model.predict(img)
    i = np.argmax(output, axis=1)
    return convertDigit(i)


def V():
    list_validation = []
    list_true = []
    path = f'../../images/dataset/AlphaBetaTubs28/ttv/validate'
    for directory in os.listdir(f'{path}'):
        for i in range(128):
            a = directory
            if a == 'apostrophe':
                a = "'"
            if a == 'divider':
                a = "-"
            if a == 'point':
                a = "."
            if a == 'slash':
                a = "/"
            if a == 'twoPoint':
                a = ":"
            list_true.append(a)
    for directory in os.listdir(f'{path}'):
        for image in os.listdir(fr'{path}/{directory}'):
            list_validation.append(To_classify(fr'{path}/{directory}/{image}'))

    y_true = list_true
    y_predict = list_validation
    c_m = confusion_matrix(y_true, y_predict)

    return c_m


def plot_confusion_matrix(c_m, target_names, title='Confusion matrix', c_map=None, normalize=False):
    accuracy = np.trace(c_m) / float(np.sum(c_m))
    mis_class = 1 - accuracy

    if c_map is None:
        c_map = plt.get_cmap('Blues')

    plt.figure(figsize=(20, 20))
    plt.imshow(c_m, interpolation='nearest', cmap=c_map)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names)
        plt.yticks(tick_marks, target_names)

    if normalize:
        c_m = c_m.astype('float') / c_m.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 1.5 if normalize else c_m.max() / 2
    for i, j in itertools.product(range(c_m.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(c_m[i, j]),
                     horizontalalignment="center",
                     color="white" if c_m[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(c_m[i, j]),
                     horizontalalignment="center",
                     color="white" if c_m[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel(f'Predicted label\naccuracy={accuracy}; mis_class={mis_class}')
    plt.show()


classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '-', '.', '/', ':', 'א', 'ב', 'ג', 'ד', 'ה', 'ו',
                'ז', 'ח', 'ט', 'י', 'ך', 'כ', 'ל', 'ם', 'מ', 'ן', 'נ', 'ס', 'ע', 'ף', 'פ', 'ץ', 'צ', 'ק', 'ר', 'ש', 'ת']
cm = V()
plot_confusion_matrix(cm, classes)
