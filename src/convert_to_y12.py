import numpy as np
import os

def convert_to_y12(algorithm, predictions, sample_name):
    sample_name = sample_name.rstrip('v')
    sample_name = sample_name.rstrip('a')
    sample_name = sample_name.rstrip('w')
    sample_name = sample_name.rstrip('.')
    # labels = ['Feedback',
    #'TL1', 'Multiple1', 'DT1', 'RS1', 'AttackLv1', 'AM1', 'Decay1Lv1', 'SustainLv1', 'Decay2Lv1',
    #'TL2', 'Multiple2', 'DT2', 'RS2', 'AttackLv2', 'AM2', 'Decay1Lv2', 'SustainLv2', 'Decay2Lv2',
    #'TL3', 'Multiple3', 'DT3', 'RS3', 'AttackLv3', 'AM3', 'Decay1Lv3', 'SustainLv3', 'Decay2Lv3',
    #'TL4', 'Multiple4', 'DT4', 'RS4', 'AttackLv4', 'AM4', 'Decay1Lv4', 'SustainLv4', 'Decay2Lv4']
    # DT is indexed 0, 1, 2, 3, -1, -2, -3, but not so in the .y12 format, so have to convert.
    for i in np.arange(0,3): 
        if predictions[3 + 9*i] == 0: # Note: both 0 and 4 are functionally the same, as tested in Deflemask.
            predictions[3 + 9*i] = 4  #       since DT ranges over only 7 values.
        if predictions[3 + 9*i] == -1:
            predictions[3 + 9*i] = 5
        if predictions[3 + 9*i] == -2:
            predictions[3 + 9*i] = 6
        if predictions[3 + 9*i] == -3:
            predictions[3 + 9*i] = 7
    output = np.zeros(128)
    output[0] = predictions[3] * 16 + predictions[2] # DT1 * 16 + Multiple1
    output[1] = predictions[1] # TL1
    output[2] = predictions[4] * 64 + predictions[5] # RS1 * 64 + Attack1
    output[3] = predictions[6] * 128 + predictions[7] # AM1 * 128 + Decay1
    output[4] = predictions[9] # Decay2_1 
    output[5] = predictions[8] * 16 + 15 # Sustain1 * 16 + Release1 (15 since we didn't use it)
    output[16] = predictions[12] * 16 + predictions[11] # DT2 * 16 + Multiple2
    output[17] = predictions[10] # TL2
    output[18] = predictions[13] * 64 + predictions[14] # RS2 * 64 + Attack2
    output[19] = predictions[15] * 128 + predictions[16] # AM2 * 128 + Decay2
    output[20] = predictions[18] # Decay2_2
    output[21] = predictions[17] * 16 + 15 # Sustain2 * 16 + Release2 (15 since we didn't use it)
    output[32] = predictions[21] * 16 + predictions[20] # DT3 * 16 + Multiple3
    output[33] = predictions[19] # TL3
    output[34] = predictions[22] * 64 + predictions[23] # RS3 * 64 + Attack3
    output[35] = predictions[24] * 128 + predictions[25] # AM3 * 128 + Decay3
    output[36] = predictions[27] # Decay2_3
    output[37] = predictions[26] * 16 + 15 # Sustain3 * 16 + Release3 (15 since we didn't use it)
    output[48] = predictions[30] * 16 + predictions[29] # DT4 * 16 + Multiple4
    output[49] = predictions[28] # TL4
    output[50] = predictions[31] * 64 + predictions[32] # RS4 * 64 + Attack4
    output[51] = predictions[33] * 128 + predictions[34] # AM4 * 128 + Decay4
    output[52] = predictions[36] # Decay2_4
    output[53] = predictions[35] * 16 + 15 # Sustain4 * 16 + Release4 (15 since we didn't use it)
    output[64] = algorithm
    output[65] = predictions[0] # feedback
    
    patchname = sample_name + '_' + algorithm + '.y12' 
    with open(patchname, 'wb') as f: 
        bytelist = [int(i).to_bytes(1,'big') for i in output]
        bytesum = bytelist[0]
        for j in np.arange(1,128):
            bytesum += bytelist[j]
        f.write(bytesum)