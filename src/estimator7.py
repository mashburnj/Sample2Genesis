import numpy as np
import os
import pandas as pd
import pickle as pk
from scipy import signal
from scipy.fft import fft
from scipy.io import wavfile
from sklearn.decomposition import PCA
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.layers import Dense
from convert_to_y12 import convert_to_y12

# Load sample
SampleName = "sample7.wav" # Audio File
SampleRate, Audiodata = wavfile.read(SampleName)

Audiodata = Audiodata[0:141120] # Want to exactly match the length of the WAVs used to train.

# Run spectral analysis
frequencies, times, spectrogram = signal.spectrogram(Audiodata, SampleRate)
del frequencies
del times
print(np.shape(spectrogram))

SampleFeatures = np.append(spectrogram.flatten(), Audiodata).reshape(1,-1)

# Load parameters for scaling data.
os.chdir('..')
os.chdir('./models/')
mean = np.loadtxt('mean7.csv', delimiter = ',')
stdev = np.loadtxt('scale7.csv', delimiter = ',')
# Z = (x - m)/s
SampleFeatures = (SampleFeatures - mean)/stdev
del mean
del stdev

# Load PCA model.
pca = pk.load(open('pca7.pkl','rb'))
print("Loaded PCA from disk")
ReducedFeatures = pca.transform(SampleFeatures)
del SampleFeatures
del pca
del spectrogram

# Load NN model.
json_file = open('model7.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model7 = model_from_json(loaded_model_json)
# load weights into new model
model7.load_weights("model7.h5")
print("Loaded model from disk")
 
#model7.compile(loss='mean_square_error', optimizer='adam', metrics=['mean_square_error'])

predictions = model7.predict(ReducedFeatures)

predictions[0][3] -= 4 # To reverse the operation done to the training set.
predictions[0][12] -= 4 # Operation was done to make DT >= 0 due to using ReLU.
predictions[0][21] -= 4
predictions[0][30] -= 4

labels = ['Feedback',
'TL1', 'Multiple1', 'DT1', 'RS1', 'AttackLv1', 'AM1', 'Decay1Lv1', 'SustainLv1', 'Decay2Lv1',
'TL2', 'Multiple2', 'DT2', 'RS2', 'AttackLv2', 'AM2', 'Decay1Lv2', 'SustainLv2', 'Decay2Lv2',
'TL3', 'Multiple3', 'DT3', 'RS3', 'AttackLv3', 'AM3', 'Decay1Lv3', 'SustainLv3', 'Decay2Lv3',
'TL4', 'Multiple4', 'DT4', 'RS4', 'AttackLv4', 'AM4', 'Decay1Lv4', 'SustainLv4', 'Decay2Lv4']

print('Predicted registers: ')

for i in np.arange(0,37):
    print(labels[i], ':', predictions[0][i], '. Rounded:', predictions[0][i].round())

convert_to_y12(7, predictions, SampleName)