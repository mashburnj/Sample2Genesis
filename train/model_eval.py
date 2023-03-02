import numpy as np
import os
import pandas as pd
from tensorflow.keras.models import Sequential, model_from_json # Will experiment with various architectures
from tensorflow.keras import layers
from rescale_output import rescale_output

def model_eval(algorithm):
    # Load training and validation data.
    os.chdir('..')
    os.chdir('./data/')
    ValidationTargets = pd.read_csv('ValRegisters'+ str(algorithm) + '.csv', index_col = 0)
    ValidationFeatures = pd.read_csv('ValSpectra'+ str(algorithm) + '.csv', index_col = 0)
    
    # This will give each output variable equal weight, rather than, say, TL overpowering everything else.
    UnusedTargets, ValidationTargets = rescale_output(ValidationTargets, ValidationTargets)

    # Load NN model.
    os.chdir('..')
    os.chdir('./models/')
    json_file = open('model'+ str(algorithm) + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights('model'+ str(algorithm) + '.h5')
    model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['mean_squared_error', 'mean_absolute_error'])
    print("Loaded model from disk")
    
    loss  = model.evaluate(ValidationFeatures, ValidationTargets)
    print('Loss on Validation Set: ', loss)
    return loss

model_eval(algorithm = 4)