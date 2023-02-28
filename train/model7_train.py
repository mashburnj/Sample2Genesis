import numpy as np
import os
import pandas as pd
import pickle as pk
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler #Can also try MinMaxScaler or MaxAbsScaler
from tensorflow.keras.models import Sequential, model_from_json # Will experiment with various architectures
from tensorflow.keras import layers

def model7_prep(use_wav: bool, use_pca: bool):
    # Load training data.
    os.chdir('..')
    os.chdir('./data/')
    RegisterTargets = pd.read_csv('SampleRegisters7.csv', index_col = 0)
    SampleFeatures = pd.read_csv('SampleSpectra7.csv', index_col = 0)
    if use_wav:
        SampleWav = pd.read_csv('SampleWav7.csv', index_col = 0)
        SampleFeatures = pd.concat([SampleFeatures, SampleWav], axis = 1, join = 'inner')
        del SampleWav
    if use_pca:
        # Have to rescale before using PCA
        scaler = StandardScaler()
        SampleFeatures = scaler.fit_transform(SampleFeatures)
        #Load PCA model for this set of data.
        os.chdir('..')
        os.chdir('./models/')
        pca = pk.load(open('pca7.pkl','rb'))
        SampleFeatures = pca.transform(SampleFeatures)
        del pca
    for DTcol in ['DT1', 'DT2', 'DT3', 'DT4']:
        RegisterTargets[DTcol] = RegisterTargets[DTcol] + 4 # Make this non-zero for ReLU.
    return SampleFeatures, RegisterTargets

def model7_train(save_to_disk: bool, TrainFeatures, TrainTargets, ValFeatures, ValTargets):
    # Building the model
    model7 = Sequential()
    model7.add(layers.Input(shape = (81141,)))
    model7.add(layers.Dense(220, activation='relu'))
    model7.add(layers.Dense(200, activation='relu'))
    model7.add(layers.Dense(180, activation='relu'))
    model7.add(layers.Dense(160, activation='relu'))
    model7.add(layers.Dense(140, activation='relu'))
    model7.add(layers.Dense(120, activation='relu'))
    model7.add(layers.Dense(100, activation='relu'))
    model7.add(layers.Dense(80, activation='relu'))
    model7.add(layers.Dense(37, activation='relu')) # 41 numerical outputs, but only 37 if we exclude release.
    # To do: experiment (more) with loss and optimizer options.
    model7.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['mean_squared_error', 'mean_absolute_error'])
    model7.fit(TrainFeatures,TrainTargets,epochs = 750, batch_size = 3)
    # To do: determine more insightful metrics. I know that MAPE is useless for my purposes, since we have zeros in our targets.
    loss  = model7.evaluate(ValFeatures, ValTargets)
    print('Loss: ', loss)
    if save_to_disk:
        # Saving model to JSON and weights to H5.
        os.chdir('..')
        os.chdir('./models/')
        model_json = model7.to_json()
        with open("model7.json", "w") as json_file:
            json_file.write(model_json)
        model7.save_weights("model7.h5")
        print("Saved model to disk")
    return loss

# If running this as a standalone, uncomment the following:
# RF, RT = model7_prep()
# model7_train(save_to_disk = True, RF, RT)