import numpy as np
import os
import pandas as pd
from scipy import signal
from scipy.io import wavfile

# Open directory with the patches in it.
os.chdir('..')
os.chdir('./val_patches/')

# Make a NP array of every y12 file in the directory
SampleList = np.array(os.listdir())
SampleList = SampleList[ np.char.endswith(SampleList, '.y12') ] # Ignore everything that's not a .y12 file.

# Make a fresh blank series.
SampleRegisters = pd.DataFrame(columns = ['Algorithm','Feedback',
                                          'TL1', 'Multiple1', 'DT1', 'RS1', 'AttackLv1', 'AM1', 'Decay1Lv1', 'SustainLv1', 'Decay2Lv1', 'ReleaseLv1',
                                          'TL2', 'Multiple2', 'DT2', 'RS2', 'AttackLv2', 'AM2', 'Decay1Lv2', 'SustainLv2', 'Decay2Lv2', 'ReleaseLv2',
                                          'TL3', 'Multiple3', 'DT3', 'RS3', 'AttackLv3', 'AM3', 'Decay1Lv3', 'SustainLv3', 'Decay2Lv3', 'ReleaseLv3',
                                          'TL4', 'Multiple4', 'DT4', 'RS4', 'AttackLv4', 'AM4', 'Decay1Lv4', 'SustainLv4', 'Decay2Lv4', 'ReleaseLv4',
                                          'Ratio1', 'Attack1', 'Decay1', 'Sustain1',
                                          'Ratio2', 'Attack2', 'Decay2', 'Sustain2',
                                          'Ratio3', 'Attack3', 'Decay3', 'Sustain3',
                                          'Ratio4', 'Attack4', 'Decay4', 'Sustain4'])

progress_count = 0

for SampleName in SampleList:
    with open(SampleName, 'rb') as y12File:
        registers = y12File.read(66) #only first 66 bytes are used
    #mask = np.array([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,
    #        1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,
    #        1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,
    #        1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,
    #        1,1], dtype=bool)
    #registersUsed = registers[mask]
    #print(registersUsed)
    #rough programming, I know, but NumPy doesn't seem to like converting byte arrays to int arrays.
    registersUsed = np.zeros(58)
    registersUsed[0] = registers[0] #Ratio1
    registersUsed[1] = registers[1] #TL1
    registersUsed[2] = registers[2] #Attack1
    registersUsed[3] = registers[3] #Decay1_1
    registersUsed[4] = registers[4] #Decay2_1
    registersUsed[5] = registers[5] #Sustain1
    registersUsed[6] = registers[16] #Ratio2
    registersUsed[7] = registers[17] #TL2
    registersUsed[8] = registers[18] #Attack2
    registersUsed[9] = registers[19] #Decay1_2
    registersUsed[10] = registers[20] #Decay2_2
    registersUsed[11] = registers[21] #Sustain2
    registersUsed[12] = registers[32] #Ratio3
    registersUsed[13] = registers[33] #TL3
    registersUsed[14] = registers[34] #Attack3
    registersUsed[15] = registers[35] #Decay1_3
    registersUsed[16] = registers[36] #Decay2_3
    registersUsed[17] = registers[37] #Sustain3
    registersUsed[18] = registers[48] #Ratio4
    registersUsed[19] = registers[49] #TL4
    registersUsed[20] = registers[50] #Attack4
    registersUsed[21] = registers[51] #Decay1_4
    registersUsed[22] = registers[52] #Decay2_4
    registersUsed[23] = registers[53] #Sustain4
    registersUsed[24] = registers[64] #Algorithm (0, full FM, through 8, just additive synth)
    registersUsed[25] = registers[65] #Feedback for Operator 1
    registersUsed[26] = registers[0] % 16 # Multiple1
    registersUsed[27] = registers[0] // 16 # DT1
    registersUsed[28] = registers[2] // 64 # RS1
    registersUsed[29] = registers[2] % 64 # Attack1
    registersUsed[30] = registers[3] // 128 # AM1 bit
    registersUsed[31] = registers[3] % 128 # Decay1
    registersUsed[32] = registers[5] // 16 # Sustain1
    registersUsed[33] = registers[5] % 16 # Release1
    registersUsed[34] = registers[16] % 16 # Multiple2
    registersUsed[35] = registers[16] // 16 # DT2
    registersUsed[36] = registers[18] // 64 # RS2
    registersUsed[37] = registers[18] % 64 # Attack2
    registersUsed[38] = registers[19] // 128 # AM2 bit
    registersUsed[39] = registers[19] % 128 # Decay2
    registersUsed[40] = registers[21] // 16 # Sustain2
    registersUsed[41] = registers[21] % 16 # Release2
    registersUsed[42] = registers[32] % 16 # Multiple3
    registersUsed[43] = registers[32] // 16 # DT3
    registersUsed[44] = registers[34] // 64 # RS3
    registersUsed[45] = registers[34] % 64 # Attack3
    registersUsed[46] = registers[35] // 128 # AM3 bit
    registersUsed[47] = registers[35] % 128 # Decay3
    registersUsed[48] = registers[37] // 16 # Sustain3
    registersUsed[49] = registers[37] % 16 # Release3
    registersUsed[50] = registers[48] % 16 # Multiple4
    registersUsed[51] = registers[48] // 16 # DT4
    registersUsed[52] = registers[50] // 64 # RS4
    registersUsed[53] = registers[50] % 64 # Attack4
    registersUsed[54] = registers[51] // 128 # AM4 bit
    registersUsed[55] = registers[51] % 128 # Decay4
    registersUsed[56] = registers[53] // 16 # Sustain4
    registersUsed[57] = registers[53] % 16 # Release4
    for i in np.arange(0,3): # DT is indexed 0, 1, 2, 3, -1, -2, -3, so have to convert.
        if registersUsed[27 + 8*i] == 4:
            registersUsed[27 + 8*i] = 0
        if registersUsed[27 + 8*i] == 5:
            registersUsed[27 + 8*i] = -1
        if registersUsed[27 + 8*i] == 6:
            registersUsed[27 + 8*i] = -2
        if registersUsed[27 + 8*i] == 7:
            registersUsed[27 + 8*i] = -3
    RowIndex = SampleName.rstrip('2')
    RowIndex = RowIndex.rstrip('1')
    RowIndex = RowIndex.rstrip('y')
    RowIndex = RowIndex.rstrip('.')
    RowIndex = RowIndex + ".wav" #This is so we don't have to fiddle with index labels in any of the estimators, where we'll import this CSV.
    SampleRow = pd.DataFrame([registersUsed], index = [RowIndex], columns = ['Ratio1', 'TL1', 'Attack1', 'Decay1', 'Decay2Lv1', 'Sustain1', 'Ratio2', 'TL2', 'Attack2', 'Decay2', 'Decay2Lv2', 'Sustain2', 'Ratio3', 'TL3', 'Attack3', 'Decay3', 'Decay2Lv3', 'Sustain3', 'Ratio4', 'TL4', 'Attack4', 'Decay4', 'Decay2Lv4', 'Sustain4', 'Algorithm','Feedback', 'Multiple1', 'DT1', 'RS1', 'AttackLv1', 'AM1', 'Decay1Lv1', 'SustainLv1', 'ReleaseLv1', 'Multiple2', 'DT2', 'RS2', 'AttackLv2', 'AM2', 'Decay1Lv2', 'SustainLv2', 'ReleaseLv2', 'Multiple3', 'DT3', 'RS3', 'AttackLv3', 'AM3', 'Decay1Lv3', 'SustainLv3', 'ReleaseLv3', 'Multiple4', 'DT4', 'RS4', 'AttackLv4', 'AM4', 'Decay1Lv4', 'SustainLv4', 'ReleaseLv4'])
    SampleRegisters = pd.concat([SampleRegisters, SampleRow])
    progress_count += 1
    print('Patches processed: ', progress_count)


os.chdir('..')
SampleRegisters.T.to_csv('ValRegisters.csv')

print('The first few samples\' registers for your viewing pleasure:')
print('Note that the last 16 columns are there for arithmetic checking, and will NOT be needed past this point.')
print(SampleRegisters.T.head())