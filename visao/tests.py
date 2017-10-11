from keras.models import Sequential,model_from_json
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

file = open("model.json","r")
loaded_model = file.read()
file.close()
loaded_model = model_from_json(loaded_model)
loaded_model.load_weights("first_try.h5")
loaded_model.compile(loss = "binary_crossentropy",
                optimizer = "rmsprop",
                metrics=["accuracy"])

print("Should be bad")
testinho = cv2.imread('3.jpg')
testinho = cv2.resize(testinho,(200,200))
testinho = np.array(testinho)
testinho = testinho.astype('float32')
testinho /= 255
testinho = np.expand_dims(testinho, axis=0)
print((loaded_model.predict(testinho)))
print(loaded_model.predict_classes(testinho))


print("Should be good")
opa = cv2.imread('2.jpg')
opa = cv2.resize(opa,(200,200))
opa = np.array(opa)
opa = opa.astype('float32')
opa /= 255
opa = np.expand_dims(opa, axis=0)

print((loaded_model.predict(opa)))
print(loaded_model.predict_classes(opa))
