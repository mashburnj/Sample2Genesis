import numpy as np
import os
import pandas as pd
#from model0_train import model0_prep, model0_train
#from model1_train import model1_prep, model1_train
#from model2_train import model2_prep, model2_train
#from model3_train import model3_prep, model3_train
#from model4_train import model4_prep, model4_train
from model5_train import model5_prep, model5_train
#from model6_train import model6_prep, model6_train
#from model7_train import model7_prep, model7_train
# Run this to train all the algorithms' models at once!
# Make changes to PCA design in the respective model#_pca.ipynb notebooks.
# Make changes to model design in the respective model#_train.py scripts.

train_algorithm = [False] * 8
# These are indexed according to their corresponding algorithms!
train_algorithm[0] = False
train_algorithm[1] = False
train_algorithm[2] = False
train_algorithm[3] = False
train_algorithm[4] = False
train_algorithm[5] = True
train_algorithm[6] = False
train_algorithm[7] = False

if train_algorithm[0]:
    RF, RT = model0_prep()
    model0_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)

if train_algorithm[1]:
    RF, RT = model1_prep()
    model1_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)

if train_algorithm[2]:
    RF, RT = model2_prep()
    model2_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)

if train_algorithm[3]:
    RF, RT = model3_prep()
    model3_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)

if train_algorithm[4]:
    RF, RT = model4_prep()
    model4_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)

if train_algorithm[5]:
    RF, RT = model5_prep()
    model5_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)

if train_algorithm[6]:
    RF, RT = model6_prep()
    model6_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)

if train_algorithm[7]:
    RF, RT = model7_prep()
    model7_train(save_to_disk = True, RedFeatures = RF, RegTargets = RT)