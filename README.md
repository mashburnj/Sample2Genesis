# SampleToYM2612
 ML model for predicting the main register settings for a single patch for the Yamaha YM2612 FM synthesis sound chip used in the Sega Genesis/Mega Drive. To be precise, it will be expected to predict the register settings for...
 1) the algorithm used (out of 8 possibilities ranging from simple 4-way additive synthesis to a single chain of 1 carrier and 3 modulators),
 2) the ratios of all operator frequencies to the fundamental frequency (determined by the note being played), and
 3) the amplitudes of the sine wave operators used.
 
 It bases its prediction on the spectrogram of an audio sample. The model will be trained using the spectra (features) and the aforementioned chip registers (targets) of samples taken from the output of a Sega Genesis (or, for the time being, the Deflemask Genesis music tracker, which is sound-accurate enough for now).

## Comments about the scope of this project:
 I'll be happy to accomplish what I've promised above, as it forms the core essence of the sound. See the "In the future" list below for details on my plan to incorporate note release behavior for each operator.

 I took a haitus in the fall, due to small sample size, but now I have ~5,600 samples, with each algorithm having at minimum 200 samples, which should be enough to train on.

### Note:
 This repository is missing the following directories referenced in the code, because the files are too large or numerous to push to GitHub:
 - data (Large CSV files containing the spectral data and raw audio data)
 - models (PCA parameters and Keras models in the JSON format)
 - patches (Collection of synth patch files in a binary format the Genesis can read)
 - wav (Recorded samples of the patch files being played in the Deflemask music tracker)

## Done so far:
 - Spectrum analyzer, with a loop version which stores all spectrograms in a single CSV (DataFrame, with wav file names as indices)
 - A WAV to CSV script, which compiles the raw audio data into a CSV.
 - A Y12 to CSV script, which interprets the bytes in each instrument file and organizes the information in a CSV (another DataFrame)
 - (Feb 17) A rescale & PCA script to reduce the raw audio data's dimensions. I chose 200 for dimension which appears to give good results, according to the plot found in the Jupyter notebook.
 - (Feb 17) Algorithm 7's neural network model in Keras, with 30 trial trainings (results are in metrics directory), using an AMD GPU with the ROCm drivers.
 - (Feb 19) Estimator script for all algorithms. It will take a WAV name and desired algorithm, load the appropriate model files, make the predictions, then output them as a Y12 synth patch file, ready for use in a Genesis music tracker.
 - (Feb 19) The main script, which searches the input directory for WAV files, then calls the estimator function 8 times for each of them, recording the results as ready-to-use Y12 files. (Currently, all but Algorithm 7's calls are dummied out, since I'm still working on the other models).

## To do:
 - The remaining ML training scripts. Will need one model for each of the 8 FM algorithms.
 - Testing and improving the models.
 
## In the future:
 - Implement training for the release behavior.
 - Switch from Deflemask to a custom Genesis ROM which will play all instruments in the training set one after the other, while Audacity records the output (either through Regen or my own Genesis*).
 - Find an FM synthesis library for Python so I can generate audio based on the predictions and compare either the spectra, raw audio output, or both, likely using the L2 error metric.
  - Rebuild this in PyTorch just for fun.
 
 \*I might need to replace the capacitors and amp circuit on it first, to ensure the cleanest possible sound output.

