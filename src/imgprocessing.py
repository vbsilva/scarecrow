from keras.models import Sequential,model_from_json
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import time
from sensors import Sensors
import os

class ImgProcessing(object):
    '''
        handles all the img processing
    '''

    def __init__(self,camera=0,debug=False):
        self.debug = debug
        self.capture = cv2.VideoCapture(camera)
        self.camera = camera
        print(os.path.abspath(__file__))
        file = open("../home/pi/Documents/scarecrow/src/model.json","r")
        file = file.read()
        self.loaded_model = model_from_json(file)
        self.loaded_model.load_weights("../home/pi/Documents/scarecrow/src/weights.h5")
        self.loaded_model.compile(loss = "binary_crossentropy",
                             optimizer = "rmsprop",
                             metrics=["accuracy"])
        
    
    def process_image(self,board):
        #self.capture.open(self.camera)
        try:
            while self.capture.isOpened() == False:
                self.capture.open(self.camera)
                time.sleep(1)
            ret, frame = self.capture.read()
            if self.debug :
                cv2.imshow("fonte", frame)
            frame = cv2.resize(frame,(200,200))
            if self.debug:
                cv2.imshow("resized", frame)
            frame = np.array(frame)
            frame = frame.astype('float32')
            frame /= 255.0
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
            board.greenLed()
            time.sleep(5)
            return classification[0][0]

        except:
            board.redLed()
            return -1
