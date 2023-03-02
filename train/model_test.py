import numpy as np
import os
import pandas as pd
from model0_train import model0_prep, model0_train
from model1_train import model1_prep, model1_train
from model2_train import model2_prep, model2_train
from model3_train import model3_prep, model3_train
from model4_train import model4_prep, model4_train
from model5_train import model5_prep, model5_train
from model6_train import model6_prep, model6_train
from model7_train import model7_prep, model7_train
# Run this to test all the algorithms' models at once!
# Make changes to PCA design in the respective model#_pca.ipynb notebooks.
# Make changes to model design in the respective model#_train.py scripts.

test_algorithm = [False] * 8
# These are indexed according to their corresponding algorithms!
test_algorithm[0] = False
test_algorithm[1] = False
test_algorithm[2] = False
test_algorithm[3] = True
test_algorithm[4] = False # I'll need to figure out a way to test this without running out of GPU RAM.
test_algorithm[5] = True
test_algorithm[6] = True
test_algorithm[7] = True

number_of_tests = 30

trial_count = 1

if test_algorithm[0]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model0_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model0_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults0.csv')
    trial_count = 1

if test_algorithm[1]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model1_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model1_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults1.csv')
    trial_count = 1

if test_algorithm[2]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model2_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model2_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults2.csv')
    trial_count = 1

if test_algorithm[3]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model3_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model3_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults3.csv')
    trial_count = 1

if test_algorithm[4]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model4_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model4_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults4.csv')
    trial_count = 1

if test_algorithm[5]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model5_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model5_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults5.csv')
    trial_count = 1

if test_algorithm[6]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model6_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model6_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults6.csv')
    trial_count = 1

if test_algorithm[7]:
    results = pd.DataFrame(columns = ['loss','mean_square_error', 'mean_absolute_error'])
    RF, RT, VF, VT = model7_prep(False)
    for i in np.arange(0,number_of_tests):
        results.loc[i] = model7_train(save_to_disk = False, TrainFeatures = RF, TrainTargets = RT, ValFeatures = VF, ValTargets = VT)
        print('Trial ', trial_count, ' complete.')
        trial_count += 1
    results.loc['Mean'] = [np.mean(results['loss']), np.mean(results['mean_square_error']), np.mean(results['mean_absolute_error'])]
    results.loc['Standard Deviation'] = [np.std(results['loss']), np.std(results['mean_square_error']), np.std(results['mean_absolute_error'])]
    os.chdir('..')
    os.chdir('./metrics/')
    results.to_csv('TestResults7.csv')