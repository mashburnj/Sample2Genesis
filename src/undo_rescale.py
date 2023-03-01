import numpy as np

# labels = ['Feedback',
    #'TL1', 'Multiple1', 'DT1', 'RS1', 'AttackLv1', 'AM1', 'Decay1Lv1', 'SustainLv1', 'Decay2Lv1',
    #'TL2', 'Multiple2', 'DT2', 'RS2', 'AttackLv2', 'AM2', 'Decay1Lv2', 'SustainLv2', 'Decay2Lv2',
    #'TL3', 'Multiple3', 'DT3', 'RS3', 'AttackLv3', 'AM3', 'Decay1Lv3', 'SustainLv3', 'Decay2Lv3',
    #'TL4', 'Multiple4', 'DT4', 'RS4', 'AttackLv4', 'AM4', 'Decay1Lv4', 'SustainLv4', 'Decay2Lv4']
    # DT is indexed 0, 1, 2, 3, -1, -2, -3, but not so in the .y12 format, so have to convert.

# AM does not need to be rescaled, since it's a bit.
def undo_rescale(PredTargets):
    for i in [3,12,21,30]: # To reverse the operation done to the training set.
        PredTargets[0][i] -= 4 # Operation was done to make DT >= 0 due to using ReLU.
    for i in [4, 13, 22, 31]:
        PredTargets[0][i] *= 3
    for i in [0, 3, 12, 21, 30]:
        PredTargets[0][i] *= 7
    for i in [2, 11, 20, 29, 8, 17, 26, 35]:
        PredTargets[0][i] *= 15
    for i in [5, 14, 23, 32, 7, 16, 25, 34, 9, 18, 27, 36]:
        PredTargets[0][i] *= 31
    for i in [1, 10, 19, 28]:
        PredTargets[0][i] *= 127
    return PredTargets