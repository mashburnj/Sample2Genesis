import numpy as np
import os
from estimator7 import estimator7
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

use_algorithm_0 = False
use_algorithm_1 = False
use_algorithm_2 = False
use_algorithm_3 = False
use_algorithm_4 = False
use_algorithm_5 = False
use_algorithm_6 = False
use_algorithm_7 = True

# Open directory with samples in it.
os.chdir('..')
os.chdir('./input/')

# next, make a NP array of every wav file in the directory
SampleList = np.array(os.listdir())
SampleList = SampleList[ np.char.endswith(SampleList, '.wav') ] #ignore everything that's not a .wav file.

for SampleName in SampleList:
    if use_algorithm_0:
        print('Algorithm 0 model not implemented and/or tested yet.')
    if use_algorithm_1:
        print('Algorithm 1 model not implemented and/or tested yet.')
    if use_algorithm_2:
        print('Algorithm 2 model not implemented and/or tested yet.')
    if use_algorithm_3:
        print('Algorithm 3 model not implemented and/or tested yet.')
    if use_algorithm_4:
        print('Algorithm 4 model not implemented and/or tested yet.')
    if use_algorithm_5:
        print('Algorithm 5 model not implemented and/or tested yet.')
    if use_algorithm_6:
        print('Algorithm 6 model not implemented and/or tested yet.')
    if use_algorithm_7:
        estimator7(SampleName)
