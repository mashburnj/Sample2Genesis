### Tests: February 26

I used mean square error and mean absolute error as the primary loss metrics for the NN models. Mean absolute percentage error doesn't work here because many target values in the training and validation sets are zero. For model 4, I decreased the number of trials to 10 because I was running TensorFlow on CPU only at the time, and that model has the largest training set by far.

For my records, here is the model's architecture. It was meant to serve as a rough starting point.

    model = Sequential()
    model.add(Dense(240, input_shape = (200,), activation='relu'))
    model.add(Dense(220, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(180, activation='relu'))
    model.add(Dense(160, activation='relu'))
    model.add(Dense(140, activation='relu'))
    model.add(Dense(120, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(37, activation='relu'))