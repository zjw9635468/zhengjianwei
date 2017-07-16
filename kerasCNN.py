import numpy
from keras.callbacks import EarlyStopping
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.layers import Dense, Dropout, Activation
from keras.layers.advanced_activations import ELU
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential, model_from_json
import os
from dataprocessing import get_data

trainX, trainY, testX, testY, validX, validY = get_data()


def process_data_CNN(X, Y):
    finalX = []
    finalY = []
    for i in range(0, len(X), 100):
        if list(Y[i:i + 100]).count('sing') == 100:
            finalX.append(X[i:i + 100])
            finalY.append(1)
        elif list(Y[i:i + 100]).count('nosing') == 100:
            finalX.append(X[i:i + 100])
            finalY.append(0)
        else:
            pass
    finalX = numpy.array(finalX)
    finalY = numpy.array(finalY)
    finalX = numpy.reshape(finalX, (-1, 1, 100, 13))
    return finalX, finalY


def build_model(X):
    nb_filters = 32  # number of convolutional filters to use
    kernel_size = (4, 4)  # convolution kernel size
    input_shape = (1, X.shape[2], X.shape[3])

    model = Sequential()
    model.add(Conv2D(nb_filters, kernel_size[0], kernel_size[1],
                     border_mode='valid', input_shape=input_shape, activation='relu'))
    model.add(Dropout(0.2))
    model.add(MaxPooling2D(pool_size=(1, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(16, kernel_size[0], kernel_size[1], activation='relu'))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dropout(0.2))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

trainX, trainY = process_data_CNN(trainX, trainY)
validX, validY = process_data_CNN(validX, validY)
testX, testY = process_data_CNN(testX, testY)


if os.path.isfile('kerasCNN.json'):
    json_file=open('kerasCNN.json','r')
    loaded_model_json=json_file.read()
    json_file.close()
    model=model_from_json(loaded_model_json)
    model.load_weights('kerasCNN.h5')
    print("Saved model to disk")
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
else:
    model = build_model(trainX)
    
    model.fit(trainX, trainY, nb_epoch=3, batch_size=64)
if not os.path.isfile('kerasCNN.json'):
    model_json = model.to_json()
    with open("kerasCNN.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights('kerasCNN.h5')

scores = model.evaluate(testX, testY, verbose=0)
print("Accuracy: %.2f%%" % (scores[1] * 100))
