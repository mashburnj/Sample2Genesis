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

def model7_prep(use_wav: bool):
    # Load training and validation data.
    os.chdir('..')
    os.chdir('./data/')
    RegisterTargets = pd.read_csv('SampleRegisters7.csv', index_col = 0)
    SampleFeatures = pd.read_csv('SampleSpectra7.csv', index_col = 0)
    ValidationTargets = pd.read_csv('ValRegisters7.csv', index_col = 0)
    ValidationFeatures = pd.read_csv('ValSpectra7.csv', index_col = 0)
    
    if use_wav:
        SampleWav = pd.read_csv('SampleWav7.csv', index_col = 0)
        SampleFeatures = pd.concat([SampleFeatures, SampleWav], axis = 1, join = 'inner')
        del SampleWav
        ValWav = pd.read_csv('ValWav7.csv', index_col = 0)
        ValidationFeatures = pd.concat([ValidationFeatures, ValWav], axis = 1, join = 'inner')
        del ValWav
        # Have to rescale before using PCA
        scaler = StandardScaler()
        SampleFeatures = scaler.fit_transform(SampleFeatures)
        ValidationFeatures = scaler.fit_transform(ValidationFeatures)
        #Load PCA model for this set of data.
        os.chdir('..')
        os.chdir('./models/')
        pca = pk.load(open('pca7.pkl','rb'))
        SampleFeatures = pca.transform(SampleFeatures)
        ValidationFeatures = pca.transform(ValidationFeatures)
        del pca
    
    # This will give each output variable equal weight, rather than, say, TL overpowering everything else.
    RegisterTargets, ValidationTargets = rescale_output(RegisterTargets, ValidationTargets)

    return SampleFeatures, RegisterTargets, ValidationFeatures, ValidationTargets

def model7_train(save_to_disk: bool, TrainFeatures, TrainTargets, ValFeatures, ValTargets):
    # Building the model
    model7 = Sequential([
        layers.Input(shape = (81141,)),
        layers.Reshape((129, 629, 1)),
        layers.Resizing(height = 129, width = 129),
        layers.Normalization(mean = 126, variance = 165000), # Stdev ~= 406. Calculated from model 7's spectra csv.
        layers.Conv2D(4, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(4, 3, activation='relu'),
        layers.Flatten(),
        layers.Dense(200, activation='relu'),
        layers.Dense(120, activation='relu'),
        layers.Dense(37, activation='relu')
    ]) # 41 numerical outputs, but only 37 if we exclude release.
    model7.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['mean_squared_error', 'mean_absolute_error'])
    model7.fit(TrainFeatures,TrainTargets,epochs = 400, batch_size = 3)
    if save_to_disk:
        # Saving model to JSON and weights to H5.
        os.chdir('..')
        os.chdir('./models/')
        model_json = model7.to_json()
        with open("model7.json", "w") as json_file:
            json_file.write(model_json)
        model7.save_weights("model7.h5")
        print("Saved model to disk")
    loss  = model7.evaluate(ValFeatures, ValTargets)
    print('Loss on Validation Set: ', loss)
    backend.clear_session()
    del model7
    gc.collect()
    return loss

# If running this as a standalone, uncomment the following:
# RF, RT, VF, VT = model7_prep(use_wav = False)
# model7_train(save_to_disk = True, RF, RT, VF, VT)