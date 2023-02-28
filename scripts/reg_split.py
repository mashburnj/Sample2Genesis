import os
import numpy as np
import pandas as pd

#open directory with the register data in it.
os.chdir('..')
os.chdir('./data/')

RegisterTargets = pd.read_csv('ValRegisters.csv', index_col = 0).T

for i in range(0,8):
    ValTargets = RegisterTargets.loc[RegisterTargets.Algorithm == i] # filter by algorithm
    ValTargets = ValTargets.drop(['Algorithm', 'Ratio1', 'Attack1', 'Decay1', 'Sustain1',
                                        'Ratio2', 'Attack2', 'Decay2', 'Sustain2',
                                        'Ratio3', 'Attack3', 'Decay3', 'Sustain3',
                                        'Ratio4', 'Attack4', 'Decay4', 'Sustain4',
                                        'ReleaseLv1', 'ReleaseLv2', 'ReleaseLv3', 'ReleaseLv4', ], axis = 'columns') # Not needed here.
    print(len(ValTargets),'patches created with algorithm ' + str(i) +' found.')
    ValTargets.to_csv('ValRegisters' + str(i) + '.csv')