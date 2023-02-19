import os
import pandas as pd

os.chdir('..')
os.chdir('./data/')

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)

RegisterTargets = pd.read_csv('SampleRegisters7.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 7 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav7.csv')
del temporary

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)
RegisterTargets = pd.read_csv('SampleRegisters6.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 6 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav6.csv')
del temporary

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)
RegisterTargets = pd.read_csv('SampleRegisters5.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 5 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav5.csv')
del temporary

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)
RegisterTargets = pd.read_csv('SampleRegisters4.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 4 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav4.csv')
del temporary

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)
RegisterTargets = pd.read_csv('SampleRegisters3.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 3 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav3.csv')
del temporary

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)
RegisterTargets = pd.read_csv('SampleRegisters2.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 2 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav2.csv')
del temporary

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)
RegisterTargets = pd.read_csv('SampleRegisters1.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 1 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav1.csv')
del temporary

BigChungus = pd.read_csv('SampleWav.csv', index_col = 0)
RegisterTargets = pd.read_csv('SampleRegisters0.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 0 found.')
temporary = BigChungus.loc[names]
del BigChungus
temporary.to_csv('SampleWav0.csv')