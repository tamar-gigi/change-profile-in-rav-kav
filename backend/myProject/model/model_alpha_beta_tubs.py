# save the final model to file
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dropout

from model.save_folders import trainTest
from keras.layers import Dense, Flatten, Conv2D
from keras.callbacks import ReduceLROnPlateau, EarlyStopping


# load train and test dataset
def load_dataset():
    trainX, trainY, testX, testY = trainTest(r'images/dataset/ABT_28/ttv/test',
                                             r'images/dataset/ABT_28/ttv/train')
    # reshape dataset to have a single channel
    trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
    testX = testX.reshape((testX.shape[0], 28, 28, 1))

    return trainX, trainY, testX, testY


# scale pixels
def prep_pixels(train, test):
    # convert from integers to floats
    train_norm = train.astype('float32')
    test_norm = test.astype('float32')
    # normalize to range 0-1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    # return normalized images
    return train_norm, test_norm


# define cnn model
def define_model():
    # Create a layer type model
    model = Sequential()
    # convolution layer-32 filters 3*3
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
    # [add this layer to decrease the loss]
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # 2 layers of convolution layer-64 filters 3*3
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    # [add this layer to decrease the loss]
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(90, (3, 3), input_shape=(28, 28, 1), activation='relu'))
    # ignore from 20% from the noironim
    model.add(Dropout(0.2))
    # flattens the input to one long vector
    model.add(Flatten())
    # another neurons layers
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    # input...
    model.add(Dense(42, activation='softmax'))
    # compile model
    opt = SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=1, min_lr=0.0001)
    early_stop = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose=0, mode='auto')

    return model, reduce_lr, early_stop


# run the test harness for evaluating a model
def run_test_harness():
    # load dataset
    trainX, trainY, testX, testY = load_dataset()
    # prepare pixel data
    trainX, testX = prep_pixels(trainX, testX)
    # define model
    model, reduce_lr, early_stop = define_model()
    # fit model
    history = model.fit(trainX, trainY, epochs=20, callbacks=[reduce_lr, early_stop], validation_data=(testX, testY))
    print("The validation accuracy is :", history.history['val_accuracy'])
    print("The training accuracy is :", history.history['accuracy'])
    print("The validation loss is :", history.history['val_loss'])
    print("The training loss is :", history.history['loss'])
    # save model
    model.save(r'model_alpha_beta_tubs.h5')


# evaluate the deep model on the test dataset
from tensorflow.keras.models import load_model


# run the test harness for evaluating a model
def run_test_harness1():
    # load dataset
    trainX, trainY, testX, testY = load_dataset()
    # prepare pixel data
    trainX, testX = prep_pixels(trainX, testX)
    # load model
    model = load_model(r'alpha_beta_tubs_model2.h5')
    # evaluate model on test dataset
    _, acc = model.evaluate(testX, testY, verbose=0)
    print('accuracy= %.3f' % (acc * 100.0))


# make a prediction for a new image.
from numpy import argmax
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model


# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, color_mode="grayscale", target_size=(28, 28))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 1 channel
    img = img.reshape(1, 28, 28, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img


def convertDigit(digit):
    arrClass = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '-', '.', '/', ':',
                'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'ך', 'כ', 'ל', 'ם', 'מ', 'ן', 'נ', 'ס', 'ע', 'ף', 'פ',
                'ץ', 'צ', 'ק', 'ר', 'ש', 'ת']
    return arrClass[int(digit)]


# load an image and predict the class
def run_example():
    # load the image
    img = load_image('predict-images/img55.png')
    # load model
    model = load_model(r'alpha_beta_tubs_model2.h5')
    # predict the class
    predict_value = model.predict(img)
    print(predict_value)
    digit = argmax(predict_value)
    print(convertDigit(digit))


def letter_image(image):
    # load the image
    img = load_image(f'{image}')
    # load model
    model = load_model(r'alpha_beta_tubs_model2.h5')
    # predict the class
    predict_value = model.predict(img)
    digit = argmax(predict_value)
    return convertDigit(digit)


if __name__ == '__main__':
    # import os
    # from model.renameFile import changeNameFile
    #
    # path = f'images/dataset/ABT_28/ttv'
    # for ttv in os.listdir(f'../{path}'):
    #     changeNameFile(f'{path}/{ttv}')

    # entry point, run the test harness
    run_test_harness()

    # entry point, run the test harness
    # run_test_harness1()

    # entry point, run the example
    # run_example()