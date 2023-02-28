import os
import numpy as np
import pandas as pd

os.chdir('..')
os.chdir('./data/')
chunksize = 560 # rows

RegisterTargets = pd.read_csv('ValRegisters7.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 7 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra7.csv')

RegisterTargets = pd.read_csv('ValRegisters6.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 6 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra6.csv')

RegisterTargets = pd.read_csv('ValRegisters5.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 5 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra5.csv')

RegisterTargets = pd.read_csv('ValRegisters4.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 4 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra4.csv')

RegisterTargets = pd.read_csv('ValRegisters3.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
chunkcount = 1
print(len(names),'patches created with algorithm 3 found.')
df = pd.DataFrame()
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra3.csv')

RegisterTargets = pd.read_csv('ValRegisters2.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 2 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra2.csv')

RegisterTargets = pd.read_csv('ValRegisters1.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 1 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra1.csv')

RegisterTargets = pd.read_csv('ValRegisters0.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 0 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('ValSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('ValSpectra0.csv')