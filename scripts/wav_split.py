import numpy as np
import os
import pandas as pd

#open directory with the raw WAV data CSV in it.
os.chdir('..')
os.chdir('./data/')

RegisterTargets = pd.read_csv('SampleRegisters7.csv', index_col = 0)

WavData = pd.read_csv('SampleWav.csv', index_col = 0).loc[RegisterTargets.index]
print(WavData.head())

WavData.to_csv('SampleWav7.csv')