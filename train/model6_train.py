import numpy as np
import os
import pandas as pd
import pickle as pk
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler #Can also try MinMaxScaler or MaxAbsScaler
from tensorflow.keras.models import Sequential, model_from_json # Will experiment with various architectures
from tensorflow.keras import layers
from rescale_output import rescale_output

def model6_prep(use_wav: bool):
    # Load training and validation data.
    os.chdir('..')
    os.chdir('./data/')
    RegisterTargets = pd.read_csv('SampleRegisters6.csv', index_col = 0)
    SampleFeatures = pd.read_csv('SampleSpectra6.csv', index_col = 0)
    ValidationTargets = pd.read_csv('ValRegisters6.csv', index_col = 0)
    ValidationFeatures = pd.read_csv('ValSpectra6.csv', index_col = 0)
    
    if use_wav:
        SampleWav = pd.read_csv('SampleWav6.csv', index_col = 0)
        SampleFeatures = pd.concat([SampleFeatures, SampleWav], axis = 1, join = 'inner')
        del SampleWav
        ValWav = pd.read_csv('ValWav6.csv', index_col = 0)
        ValidationFeatures = pd.concat([ValidationFeatures, ValWav], axis = 1, join = 'inner')
        del ValWav
        # Have to rescale before using PCA
        scaler = StandardScaler()
        SampleFeatures = scaler.fit_transform(SampleFeatures)
        ValidationFeatures = scaler.fit_transform(ValidationFeatures)
        #Load PCA model for this set of data.
        os.chdir('..')
        os.chdir('./models/')
        pca = pk.load(open('pca6.pkl','rb'))
        SampleFeatures = pca.transform(SampleFeatures)
        ValidationFeatures = pca.transform(ValidationFeatures)
        del pca
    
    # This will give each output variable equal weight, rather than, say, TL overpowering everything else.
    RegisterTargets, ValidationTargets = rescale_output(RegisterTargets, ValidationTargets)

    return SampleFeatures, RegisterTargets, ValidationFeatures, ValidationTargets

def model6_train(save_to_disk: bool, TrainFeatures, TrainTargets, ValFeatures, ValTargets):
    # Building the model
    model6 = Sequential([
        layers.Input(shape = (81141,)),
        layers.Reshape((129, 629, 1)),
        layers.Resizing(height = 129, width = 129),
        layers.Normalization(mean = 126, variance = 165000), # Stdev ~= 406. Calculated from model 6's spectra csv.
        layers.Conv2D(4, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(4, 3, activation='relu'),
        layers.Flatten(),
        layers.Dense(200, activation='relu'),
        layers.Dense(120, activation='relu'),
        layers.Dense(37, activation='relu')
    ]) # 41 numerical outputs, but only 37 if we exclude release.
    model6.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['mean_squared_error', 'mean_absolute_error'])
    if save_to_disk:
        # Saving model to JSON and weights to H5.
        os.chdir('..')
        os.chdir('./models/')
        model_json = model6.to_json()
        with open("model6.json", "w") as json_file:
            json_file.write(model_json)
        model6.save_weights("model6.h5")
        print("Saved model to disk")
    model6.fit(TrainFeatures,TrainTargets,epochs = 400, batch_size = 3)
    loss  = model6.evaluate(ValFeatures, ValTargets)
    print('Loss on Validation Set: ', loss)
    return loss

# If running this as a standalone, uncomment the following:
# RF, RT, VF, VT = model6_prep(use_wav = False)
# model6_train(save_to_disk = True, RF, RT, VF, VT)