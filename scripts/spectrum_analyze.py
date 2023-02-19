import numpy as np
import os
import pandas as pd
from scipy import signal
from scipy.io import wavfile
""" The objective of this is to find the full spectrogram,
    since the HPS approach is currently not working.""";

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

index = pd.Index(SampleList)
SampleSpectra = pd.DataFrame(columns = np.arange(0,81141))
# 0, 
# For this approach, use available Python packages to extract full spectrogram.
# Will likely use a CNN to mind the "shifts" in frequencies caused by pitch.
progress_count = 0

for SampleName in SampleList:
    SampleRate, Audiodata = wavfile.read(SampleName)
    if dont_use_release:
        Audiodata = Audiodata[0:len(Audiodata)//2]
    frequencies, times, spectrogram = signal.spectrogram(Audiodata, SampleRate)
    print(np.shape(spectrogram))
    SampleSpectra.loc[SampleName] = spectrogram.flatten()#reshape(1,81141)
    progress_count += 1
    print('Samples processed: ', progress_count)

os.chdir('..')
SampleSpectra.to_csv('SampleSpectra.csv')

print(SampleSpectra.head())