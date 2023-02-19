import os
import numpy as np
import pandas as pd

os.chdir('..')
os.chdir('./data/')
chunksize = 565 # rows

RegisterTargets = pd.read_csv('SampleRegisters7.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 7 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra7.csv')

RegisterTargets = pd.read_csv('SampleRegisters6.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 6 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra6.csv')

RegisterTargets = pd.read_csv('SampleRegisters5.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 5 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra5.csv')

RegisterTargets = pd.read_csv('SampleRegisters4.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 4 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra4.csv')

RegisterTargets = pd.read_csv('SampleRegisters3.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
chunkcount = 1
print(len(names),'patches created with algorithm 3 found.')
df = pd.DataFrame()
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra3.csv')

RegisterTargets = pd.read_csv('SampleRegisters2.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 2 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra2.csv')

RegisterTargets = pd.read_csv('SampleRegisters1.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 1 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra1.csv')

RegisterTargets = pd.read_csv('SampleRegisters0.csv', index_col = 0)
names = RegisterTargets.index
del RegisterTargets
print(len(names),'patches created with algorithm 0 found.')
df = pd.DataFrame()
chunkcount = 1
for chunk in pd.read_csv('SampleSpectra.csv', index_col = 0, chunksize = chunksize):
    print('Chunk ',chunkcount,' loaded.')
    chunkcount += 1
    indexset = set(chunk.index)
    namestemp = [i for i in names if i in indexset]
    temporary = chunk.loc[namestemp]
    df = pd.concat([df,temporary])
df.sort_index().to_csv('SampleSpectra0.csv')