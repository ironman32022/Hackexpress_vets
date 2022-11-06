import tensorflow as tf
import cv2
import numpy as np



def cnn(image_path):
    image =cv2.imread(image_path, cv2.IMREAD_COLOR)
    print(image_path)
    print(image)
    
    image = cv2.resize(image, (256,256))
    image = image.reshape((1,256,256,3))
    
   
    model = tf.keras.models.load_model('cnn.h5')
    predict = model.predict(image,verbose=1)
    print(predict)
    print(predict[0])
    print(max(predict[0]))

    if np.argmax(predict[0]) >0.5:
        result='virus'
        return result
    else:
        result='healthy'
        return result
        

model = tf.keras.models.load_model('cnn.h5')