import numpy as np
import os
import pandas as pd
import pickle as pk
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler #Can also try MinMaxScaler or MaxAbsScaler
from tensorflow.keras.models import Sequential, model_from_json # Will experiment with various architectures
from tensorflow.keras.layers import Dense

def model0_prep():
    # Load training data.
    os.chdir('..')
    os.chdir('./data/')
    RegisterTargets = pd.read_csv('SampleRegisters0.csv', index_col = 0)
    SampleFeatures = pd.read_csv('SampleSpectra0.csv', index_col = 0)
    SampleWav = pd.read_csv('SampleWav0.csv', index_col = 0)
    SampleFeatures = pd.concat([SampleFeatures, SampleWav], axis = 1, join = 'inner')
    del SampleWav
    # Have to rescale before using PCA
    scaler = StandardScaler()
    SampleFeatures = scaler.fit_transform(SampleFeatures)
    # Load PCA model for this set of data.
    os.chdir('..')
    os.chdir('./models/')
    pca = pk.load(open('pca0.pkl','rb'))
    ReducedFeatures = pca.transform(SampleFeatures)
    del SampleFeatures
    del pca
    for DTcol in ['DT1', 'DT2', 'DT3', 'DT4']:
        RegisterTargets[DTcol] = RegisterTargets[DTcol] + 4 # Make this non-zero for ReLU.
    return ReducedFeatures, RegisterTargets

def model0_train(save_to_disk: bool, RedFeatures, RegTargets):
    # Building the model
    model0 = Sequential()
    model0.add(Dense(240, input_shape = (200,), activation='relu'))
    model0.add(Dense(220, activation='relu'))
    model0.add(Dense(200, activation='relu'))
    model0.add(Dense(180, activation='relu'))
    model0.add(Dense(160, activation='relu'))
    model0.add(Dense(140, activation='relu'))
    model0.add(Dense(120, activation='relu'))
    model0.add(Dense(100, activation='relu'))
    model0.add(Dense(80, activation='relu'))
    model0.add(Dense(37, activation='relu')) # 41 numerical outputs, but only 37 if we exclude release.
    # To do: experiment (more) with loss and optimizer options.
    model0.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['mean_squared_error', 'mean_absolute_error'])
    model0.fit(RedFeatures,RegTargets,epochs = 750, batch_size = 3)
    # To do: determine more insightful metrics. I know that MAPE is useless for my purposes, since we have zeros in our targets.
    loss  = model0.evaluate(RedFeatures, RegTargets)
    print('Loss: ', loss)
    if save_to_disk:
        # Saving model to JSON and weights to H5.
        os.chdir('..')
        os.chdir('./models/')
        model_json = model0.to_json()
        with open("model0.json", "w") as json_file:
            json_file.write(model_json)
        model0.save_weights("model0.h5")
        print("Saved model to disk")
    return loss

# If running this as a standalone, uncomment the following:
# RF, RT = model0_prep()
# model0_train(save_to_disk = True, RF, RT)