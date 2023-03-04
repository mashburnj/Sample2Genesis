import gc
import numpy as np
import os
import pandas as pd
import pickle as pk
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler #Can also try MinMaxScaler or MaxAbsScaler
from tensorflow.keras.models import Sequential, model_from_json # Will experiment with various architectures
from tensorflow.keras import layers
from tensorflow.keras import backend
from rescale_output import rescale_output

def model4_prep(use_wav: bool):
    # Load training and validation data.
    os.chdir('..')
    os.chdir('./data/')
    RegisterTargets = pd.read_csv('SampleRegisters4.csv', index_col = 0)
    SampleFeatures = pd.read_csv('SampleSpectra4.csv', index_col = 0)
    ValidationTargets = pd.read_csv('ValRegisters4.csv', index_col = 0)
    ValidationFeatures = pd.read_csv('ValSpectra4.csv', index_col = 0)
    
    if use_wav:
        SampleWav = pd.read_csv('SampleWav4.csv', index_col = 0)
        SampleFeatures = pd.concat([SampleFeatures, SampleWav], axis = 1, join = 'inner')
        del SampleWav
        ValWav = pd.read_csv('ValWav4.csv', index_col = 0)
        ValidationFeatures = pd.concat([ValidationFeatures, ValWav], axis = 1, join = 'inner')
        del ValWav
        # Have to rescale before using PCA
        scaler = StandardScaler()
        SampleFeatures = scaler.fit_transform(SampleFeatures)
        ValidationFeatures = scaler.fit_transform(ValidationFeatures)
        #Load PCA model for this set of data.
        os.chdir('..')
        os.chdir('./models/')
        pca = pk.load(open('pca4.pkl','rb'))
        SampleFeatures = pca.transform(SampleFeatures)
        ValidationFeatures = pca.transform(ValidationFeatures)
        del pca
    
    # This will give each output variable equal weight, rather than, say, TL overpowering everything else.
    RegisterTargets, ValidationTargets = rescale_output(RegisterTargets, ValidationTargets)

    return SampleFeatures, RegisterTargets, ValidationFeatures, ValidationTargets

def model4_train(save_to_disk: bool, TrainFeatures, TrainTargets, ValFeatures, ValTargets):
    # Building the model
    model4 = Sequential([
        layers.Input(shape = (81141,)),
        layers.Reshape((129, 629, 1)),
        layers.Resizing(height = 129, width = 129),
        layers.Normalization(mean = 126, variance = 165000), # Stdev ~= 406. Calculated from model 4's spectra csv.
        layers.Conv2D(4, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(4, 3, activation='relu'),
        layers.Flatten(),
        layers.Dense(200, activation='relu'),
        layers.Dense(120, activation='relu'),
        layers.Dense(37, activation='relu')
    ]) # 41 numerical outputs, but only 37 if we exclude release.
    model4.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['mean_squared_error', 'mean_absolute_error'])
    model4.fit(TrainFeatures,TrainTargets,epochs = 400, batch_size = 3)
    # Have to save temp model files, then flush GPU RAM, then reload before validation
    # because I've only got 2 GB of GPU RAM to work with...
    os.chdir('..')
    os.chdir('./models/')
    # Saving temp model to disk
    model_json = model4.to_json()
    with open("model4temp.json", "w") as json_file:
        json_file.write(model_json)
    model4.save_weights("model4temp.h5")
    # Saving model to disk
    if save_to_disk:
        # Saving model to JSON and weights to H5.
        os.chdir('..')
        os.chdir('./models/')
        model_json = model4.to_json()
        with open("model4.json", "w") as json_file:
            json_file.write(model_json)
        model4.save_weights("model4.h5")
        print("Saved model to disk")
    # Saving model to JSON and weights to H5.
    backend.clear_session()
    del model4
    gc.collect()
    # Reloading temp model after clearing GPU RAM.
    json_file = open('model'+ str(algorithm) + 'temp.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model4 = model_from_json(loaded_model_json)
    # load weights into new model
    model4.load_weights('model'+ str(algorithm) + 'temp.h5')
    model4.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['mean_squared_error', 'mean_absolute_error'])
    loss  = model4.evaluate(ValFeatures, ValTargets)
    print('Loss on Validation Set: ', loss)
    backend.clear_session()
    del model4
    gc.collect()
    return loss

# If running this as a standalone, uncomment the following:
# RF, RT, VF, VT = model4_prep(use_wav = False)
# model4_train(save_to_disk = True, RF, RT, VF, VT)