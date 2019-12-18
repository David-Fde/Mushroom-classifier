import os
import json
from keras.models import model_from_json
import cv2
import numpy as np
from keras.models import load_model


def change_name_file(mushroom_name):
    i = 1
    path = f"Input/Mushroom-images/{mushroom_name}/"
    for filename in os.listdir(path):
        print(filename)
        dst = f"{mushroom_name}" + str(i) + ".jpeg"
        src = path + filename
        dst = path + dst
        os.rename(src, dst)
        i += 1


CLASSES = ['Amanita-cesarea', 'Amanita-muscaria',
           'Amanita-phalloides', 'Boletus-edulis', 'Niscalo']


def predict(image_dir, model_dir, weight_dir):
    '''Predict the disease of the given photo'''
    # load json and create model
    with open(model_dir, 'r') as f:
        model_json = json.load(f)
    loaded_model = model_from_json(model_json)
    loaded_model.load_weights(weight_dir)
    # image processing and recognition
    default_image_size = tuple((256, 256))
    img = cv2.imread(image_dir) / 255
    img = cv2.resize(img, default_image_size)
    np_image_li = np.asarray(img)
    npp_image = np.expand_dims(np_image_li, axis=0)
    result = loaded_model.predict(npp_image)
    itemindex = np.where(result == np.max(result))

    #print('\n' + "Probability: "+str(np.max(result)) + ' ====> ' + CLASSES[itemindex[1][0]] + '\n')
    #prediction = str('\n' + "Probability: " + str(np.max(result)) + ' ====> ' + CLASSES[itemindex[1][0]] + '\n')
    return {"Probability:": str(np.max(result)) + ' ====> ' + CLASSES[itemindex[1][0]]}
