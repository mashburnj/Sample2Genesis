import numpy as np
import os
from estimator import estimator
"""Instructions:
There are 8 booleans, one for each algorithm model. If there is an algorithm you do not
wish to use, change it to False. Put all WAV samples you wish to make predicted patches
for into the input directory.
Make sure that all of them are in MONO, and their durations are at least 3.21 seconds
(anything past that will be truncated). It sounds oddly specific, but the models were
trained on fixed length WAV files consisting of sounds played for 4 beats in the
Deflemask tracker under the default tempo.) Use Audacity if you need to resize or convert.
When the predictors are finished, you will find the patch files in the output directory.
"""
use_algorithm = [False] * 8
# These are indexed according to their corresponding algorithms!
use_algorithm[0] = True
use_algorithm[1] = True
use_algorithm[2] = True
use_algorithm[3] = True
use_algorithm[4] = True
use_algorithm[5] = True
use_algorithm[6] = True
use_algorithm[7] = True

# Open directory with samples in it.
os.chdir('..')
os.chdir('./input/')

# next, make a NP array of every wav file in the directory
SampleList = np.array(os.listdir())
SampleList = SampleList[ np.char.endswith(SampleList, '.wav') ] #ignore everything that's not a .wav file.

for SampleName in SampleList:
    for i in range(8):
        if use_algorithm[i]:
            estimator(SampleName, i)
            os.chdir('..')
            os.chdir('./input/')