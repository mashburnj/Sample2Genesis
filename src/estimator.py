import numpy as np
import os
import pandas as pd
import pickle as pk
from scipy import signal
from scipy.fft import fft
from scipy.io import wavfile
from sklearn.decomposition import PCA
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras import layers
from convert_to_y12 import convert_to_y12

def estimator(SampleName: str, algorithm: int):
    # Load sample
    SampleRate, Audiodata = wavfile.read(SampleName)

    Audiodata = Audiodata[0:141120] # Want to exactly match the length of the WAVs used to train.

    # Run spectral analysis
    frequencies, times, spectrogram = signal.spectrogram(Audiodata, SampleRate)
    del frequencies
    del times
    SampleFeatures = spectrogram.flatten()
    print(np.shape(SampleFeatures))

    # SampleFeatures = np.append(spectrogram.flatten(), Audiodata).reshape(1,-1)

    # Load parameters for scaling data.
    # mean = np.loadtxt('mean'+ str(algorithm) + '.csv', delimiter = ',')
    # stdev = np.loadtxt('scale' + str(algorithm) + '.csv', delimiter = ',')
    # Z = (x - m)/s
    # SampleFeatures = (SampleFeatures - mean)/stdev
    # del mean
    # del stdev

    # Load PCA model.
    #pca = pk.load(open('pca'+ str(algorithm) + '.pkl','rb'))
    #print("Loaded PCA from disk")
    #ReducedFeatures = pca.transform(SampleFeatures)
    #del SampleFeatures
    #del pca
    #del spectrogram

    # Load NN model.
    os.chdir('..')
    os.chdir('./models/')
    json_file = open('model'+ str(algorithm) + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights('model'+ str(algorithm) + '.h5')
    print("Loaded model from disk")
    
    #model.compile(loss='mean_square_error', optimizer='adam', metrics=['mean_square_error'])

    predictions = model.predict(SampleFeatures)

    predictions[0][3] -= 4 # To reverse the operation done to the training set.
    predictions[0][12] -= 4 # Operation was done to make DT >= 0 due to using ReLU.
    predictions[0][21] -= 4
    predictions[0][30] -= 4
    
    convert_to_y12(algorithm, predictions[0].round(), SampleName)