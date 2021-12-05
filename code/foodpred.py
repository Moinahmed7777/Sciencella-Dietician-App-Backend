# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:48:17 2021

@author: Necro
"""
#from tflite_model_maker.image_classifier import DataLoader
#from tf.lite import Interpreter
import tensorflow as tf
from PIL import Image
from numpy import asarray
import numpy as np
import os  
from flask_restful import Resource, reqparse,abort,fields,marshal_with,request
from pathlib import Path




#class pred(Resource):
    #post
def pred(X):
    
    img = Image.open(X.stream)
    #for v2l_21k
    new_width  = 384
    new_height = 384
    #for v2xl_21k
    #new_width  = 512
    #new_height = 512
    #new_width  = 480
    #new_height = 480
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.show()
    numpydata = asarray(img)
    #expand the dimensions according to the required tflite model input  
    npd = np.expand_dims(numpydata, axis=0)
    print("1")
    #load the tflite model
    #C:\\Users\\Moina\\Desktop\\imgclass_test\\models\\V2XL21kft1k\\
    TFLITE_FILE_PATH = './model.tflite'
    tflite_interpreter = tf.lite.Interpreter(model_path=TFLITE_FILE_PATH)
    input_details = tflite_interpreter.get_input_details()
    output_details = tflite_interpreter.get_output_details()
    print("2")
    tflite_interpreter.allocate_tensors()
    print("3")
    tflite_interpreter.set_tensor(input_details[0]['index'], npd)
    print("4")
    tflite_interpreter.invoke()
    print("5")
    tflite_model_predictions = tflite_interpreter.get_tensor(output_details[0]['index'])
    
    print(tflite_model_predictions)
    #print("Prediction results shape:", tflite_model_predictions.shape)
    prediction_classes = np.argmax(tflite_model_predictions, axis=1)
    #print(type(prediction_classes))
    
    #foodclasses={ 0:"apple pie",1:"baby back ribs",2:"baklava",3:"beef carpaccio",4:"beef tartare"}
        
    foodclasses101= {0: 'apple_pie', 1: 'baby_back_ribs', 2: 'baklava', 3: 'beef_carpaccio', 4: 'beef_tartare', 5: 'beet_salad', 6: 'beignets', 7: 'bibimbap', 8: 'bread_pudding', 9: 'breakfast_burrito', 10: 'bruschetta', 11: 'caesar_salad', 12: 'cannoli', 13: 'caprese_salad', 14: 'carrot_cake', 15: 'ceviche', 16: 'cheesecake', 17: 'cheese_plate', 18: 'chicken_curry', 19: 'chicken_quesadilla', 20: 'chicken_wings', 21: 'chocolate_cake', 22: 'chocolate_mousse', 23: 'churros', 24: 'clam_chowder', 25: 'club_sandwich', 26: 'crab_cakes', 27: 'creme_brulee', 28: 'croque_madame', 29: 'cup_cakes', 30: 'deviled_eggs', 31: 'donuts', 32: 'dumplings', 33: 'edamame', 34: 'eggs_benedict', 35: 'escargots', 36: 'falafel', 37: 'filet_mignon', 38: 'fish_and_chips', 39: 'foie_gras', 40: 'french_fries', 41: 'french_onion_soup', 42: 'french_toast', 43: 'fried_calamari', 44: 'fried_rice', 45: 'frozen_yogurt', 46: 'garlic_bread', 47: 'gnocchi', 48: 'greek_salad', 49: 'grilled_cheese_sandwich', 50: 'grilled_salmon', 51: 'guacamole', 52: 'gyoza', 53: 'hamburger', 54: 'hot_and_sour_soup', 55: 'hot_dog', 56: 'huevos_rancheros', 57: 'hummus', 58: 'ice_cream', 59: 'lasagna', 60: 'lobster_bisque', 61: 'lobster_roll_sandwich', 62: 'macaroni_and_cheese', 63: 'macarons', 64: 'miso_soup', 65: 'mussels', 66: 'nachos', 67: 'omelette', 68: 'onion_rings', 69: 'oysters', 70: 'pad_thai', 71: 'paella', 72: 'pancakes', 73: 'panna_cotta', 74: 'peking_duck', 75: 'pho', 76: 'pizza', 77: 'pork_chop', 78: 'poutine', 79: 'prime_rib', 80: 'pulled_pork_sandwich', 81: 'ramen', 82: 'ravioli', 83: 'red_velvet_cake', 84: 'risotto', 85: 'samosa', 86: 'sashimi', 87: 'scallops', 88: 'seaweed_salad', 89: 'shrimp_and_grits', 90: 'spaghetti_bolognese', 91: 'spaghetti_carbonara', 92: 'spring_rolls', 93: 'steak', 94: 'strawberry_shortcake', 95: 'sushi', 96: 'tacos', 97: 'takoyaki', 98: 'tiramisu', 99: 'tuna_tartare', 100: 'waffles'}
    prediction = foodclasses101[prediction_classes[0]]
    
    return prediction

