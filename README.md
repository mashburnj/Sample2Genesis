# SampleToYM2612
 ML model for predicting the main register settings for a single patch for the Yamaha YM2612 FM synthesis sound chip used in the Sega Genesis/Mega Drive. To be precise, it will be expected to predict the register settings for...
 1) the algorithm used (out of 8 possibilities ranging from simple 4-way additive synthesis to a single chain of 1 carrier and 3 modulators),
 2) the ratios of all operator frequencies to the fundamental frequency (determined by the note being played), and
 3) the amplitudes of the sine wave operators used.
 
 It bases its prediction on the spectrum of an audio sample. The model will be trained using the spectra (features) and the aforementioned chip registers (targets) of samples taken from the output of a Sega Genesis.

## Comments about the scope of this project:
 I'll be happy to accomplish what I've promised above, as it forms the core essence of the sound. See the "In the future" list below for details on my plan to incorporate note release behavior for each operator.

 I took a haitus in the fall, due to small sample size, but now I have ~5,600 samples, with each algorithm having at minimum 200 samples, which should be enough to train on.

## Done so far:
 - Spectrum analyzer, with a loop version which stores all spectrograms in a single CSV (DataFrame, with wav file names as indices)
 - A WAV to CSV script, which compiles the raw audio data into a CSV. (I may not actually use this. I'll try training without the raw data and see how it does, since I have full spectrograms).
 - A Y12 to CSV script, which interprets the bytes in each instrument file and organizes the information in a CSV (another DataFrame)
 
 
## To do:
 - Algorithm 7's training script. This is the simplest FM algorithm: just additive synthesis with feedback on Operator 1.
 - The remaining ML training scripts. Will need one model for each of the 8 FM algorithms.
 - Testing and improving the models.
 - The ML prediction software. Has to be able to extract the raw audio and its spectrum, then output 8 different predictions. Needs the above 8 models trained first.
 - If I use the raw audio data, a WAV CSV dimension reducer script, likely using PCA. With my old sample set, 64 components gave a 91% explained variance rating, with harshly diminishing returns beyond that point. If I use raw data, I'd like a similar rate.
 
## In the future:
 - Implement training for the release behavior.
 - Switch from Deflemask to a custom Genesis ROM which will play all instruments in the training set one after the other, while Audacity records the output (either through Regen or a Genesis).
 - Find an FM synthesis library for Python so I can generate audio based on the predictions and compare either the spectra, raw audio output, or both, likely using least-squares.