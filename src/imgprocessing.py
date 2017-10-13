from keras.models import Sequential,model_from_json
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import time

class ImgProcessing(object):
    '''
        handles all the img processing
    '''

    def __init__(self,camera=0,debug=False):
        self.debug = debug
        self.capture = cv2.VideoCapture(camera)
        file = open("model.json","r")
        file = file.read()
        self.loaded_model = model_from_json(file)
        self.loaded_model.load_weights("weights.h5")
        self.loaded_model.compile(loss = "binary_crossentropy",
                             optimzer = "rmsprop",
                             metrics=["accuracy"])
    
    def process_image(self):
        ret, frame = self.capture.read()
        if self.debug :
            cv2.imshow("fonte", frame)
        cv2.resize(frame,(200,200))
        if self.debug:
            cv2.imshow("resized", frame)
        frame = np.array(frame)
        frame = frame.astype('float32')
        frame /= 255
        frame = np.expand_dims(frame, axis = 0)
        predict = self.loaded_model.predict(frame)
        if self.debug:
            print(predict)
        classification = self.loaded_model.predict_classes(frame)
        if self.debug:
            print(classification)
        if self.debug:
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return classification
        time.sleep(5)
