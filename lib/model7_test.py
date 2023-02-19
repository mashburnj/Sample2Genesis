import numpy as np
import os
import pandas as pd
from model7_train import model7_prep, model7_train

number_of_tests = 30

results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])

RF, RT = model7_prep()

for i in np.arange(0,number_of_tests):
    results.loc[i] = model7_train(save_to_disk = False, RedFeatures = RF, RegTargets = RT)

results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
os.chdir('..')
os.chdir('./metrics/')
results.to_csv('TestResults7.csv')