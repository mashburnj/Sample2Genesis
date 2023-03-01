import numpy as np
import pandas as pd

# labels = ['Feedback',
    #'TL1', 'Multiple1', 'DT1', 'RS1', 'AttackLv1', 'AM1', 'Decay1Lv1', 'SustainLv1', 'Decay2Lv1',
    #'TL2', 'Multiple2', 'DT2', 'RS2', 'AttackLv2', 'AM2', 'Decay1Lv2', 'SustainLv2', 'Decay2Lv2',
    #'TL3', 'Multiple3', 'DT3', 'RS3', 'AttackLv3', 'AM3', 'Decay1Lv3', 'SustainLv3', 'Decay2Lv3',
    #'TL4', 'Multiple4', 'DT4', 'RS4', 'AttackLv4', 'AM4', 'Decay1Lv4', 'SustainLv4', 'Decay2Lv4']
    # DT is indexed 0, 1, 2, 3, -1, -2, -3, but not so in the .y12 format, so have to convert.

# Note: these variables range from 0 to pwr of 2.
# We want, for instance, predicted Feedback of 7 vs actual of 0 to have 1.0 error
# AM is just a bit, so no need to rescale. Incorrect predictions will already have 1.0 error.
def rescale_output(RegTargets, ValTargets):
    for DTcol in ['DT1', 'DT2', 'DT3', 'DT4']:
        RegTargets[DTcol] = RegTargets[DTcol] + 4 # Make this non-zero for ReLU.
        ValTargets[DTcol] = ValTargets[DTcol] + 4 # Make this non-zero for ReLU.
    for range4 in ['RS1', 'RS2', 'RS3', 'RS4']:
        RegTargets[range8] = RegTargets[range8] / 3.0
        ValTargets[range8] = ValTargets[range8] / 3.0
    for range8 in ['Feedback', 'DT1', 'DT2', 'DT3', 'DT4']:
        RegTargets[range8] = RegTargets[range8] / 7.0
        ValTargets[range8] = ValTargets[range8] / 7.0
    for range16 in ['Multiple1', 'Multiple2', 'Multiple3', 'Multiple4',
                    'SustainLv1', 'SustainLv2', 'SustainLv3', 'SustainLv4']:
        RegTargets[range8] = RegTargets[range8] / 15.0
        ValTargets[range8] = ValTargets[range8] / 15.0
    for range32 in ['AttackLv1', 'AttackLv2', 'AttackLv3', 'AttackLv4',
                    'Decay1Lv1', 'Decay1Lv2', 'Decay1Lv3', 'Decay1Lv4',
                    'Decay2Lv1', 'Decay2Lv2', 'Decay2Lv3', 'Decay2Lv4']:
        RegTargets[range8] = RegTargets[range8] / 31.0
        ValTargets[range8] = ValTargets[range8] / 31.0
    for range128 in ['TL1', 'TL2', 'TL3', 'TL4']:
        RegTargets[range8] = RegTargets[range8] / 127.0
        ValTargets[range8] = ValTargets[range8] / 127.0
    return RegTargets, ValTargets