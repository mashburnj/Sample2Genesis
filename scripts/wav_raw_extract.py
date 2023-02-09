import numpy as np
import os
import pandas as pd
from scipy import signal
from scipy.io import wavfile
""" Note: Each sample in my set releases the note halfway.
False -> we train with the release behavior (not a good idea).
True -> we don't, and we only use the first half of each sample.
"""
dont_use_release = True

# Open directory with samples in it.
os.chdir('..')
os.chdir('./wav/')

# next, make a NP array of every wav file in the directory
SampleList = np.array(os.listdir())
SampleList = SampleList[ np.char.endswith(SampleList, '.wav') ] #ignore everything that's not a .wav file.

index = pd.Index(np.arange(0,141419))
columns = pd.Index(SampleList)
SampleWav = pd.DataFrame(0, index = index, columns=columns)

progress_count = 0

for SampleName in SampleList:
    SampleRate, Audiodata = wavfile.read(SampleName)
    if dont_use_release:
        Audiodata = Audiodata[0:len(Audiodata)//2]
    SampleWav[SampleName] = Audiodata
    progress_count += 1
    print('Samples processed: ', progress_count)

os.chdir('..')
SampleWav.to_csv('SampleWav.csv')

print(SampleWav.head())