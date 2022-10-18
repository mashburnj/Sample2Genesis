# SampleToYM2612
 ML model for predicting the main register settings for a single patch for the Yamaha YM2612 FM synthesis sound chip used in the Sega Genesis/Mega Drive. To be precise, it will be expected to predict the register settings for...
 1) the algorithm used (out of 8 possibilities ranging from simple 4-way additive synthesis to a single chain of 1 carrier and 3 modulators),
 2) the ratios of all operator frequencies to the fundamental frequency (determined by the note being played), and
 3) the amplitudes of the sine wave operators used.
 
 It bases its prediction on the spectrum of an audio sample. The model will be trained using the spectra (features) and the aforementioned chip registers (targets) of samples taken from the output of a Sega Genesis.

## Comments about the scope of this project:
 The YM2612 chip has several more registers for EACH operator, including attack, decay, and sustain. For now, I'll be assuming all four operators have the same attack, decay, and sustain behavior, as well as simple release behavior.
 
 I'll be happy to accomplish what I've promised above, as it forms the core essence of the sound. See the "In the future" list below for details on my plan to incorporate separate ADSR values for each operator- it involves a much more detailed spectral analysis, as well as sample data which includes release behavior (starting at the exact same point in time across all audio samples).

## Done so far:
 - Spectrum analyzer, with a loop version which stores all spectra in a single CSV (DataFrame, with wav file names as indices)
 - A WAV to CSV script, which compiles the raw audio data into a CSV.
 - A WAV CSV dimension reducer script. I used PCA with 64 components, which gave a 91% explained variance rating, with harshly diminishing returns beyond that point. Not bad for a ~35,000-dimensional dataset.
 - A Y12 to CSV script, which interprets the bytes in each instrument file and organizes the information in a CSV (another DataFrame)
  - Algorithm 7's training script. This is the simplest FM algorithm: just additive synthesis with feedback on Operator 1.
 
## To do:
 - The remaining ML training scripts. Will need one model for each of the 8 FM algorithms.
 - The ML prediction script. Has to be able to extract the raw audio and its spectrum, then give 8 different predictions.
 
## In the future:
 - Take more sophisticated samples, with a common time to release the "key" to observe the release behavior.
 - Switch from Deflemask to a custom Genesis ROM which will play all instruments in the training set one after the other, while Audacity records the output (either through Regen or a Genesis).
 - Chop up the samples into 8ths or 16ths, and run spectral analysis on each, to get an idea of how each operator changes over time.
 - Find an FM synthesis library for Python so I can generate audio based on the predictions and compare either the spectra, raw audio output, or both, likely using the L2-metric.
 
# Project on hold as of October 17th:
I need more sample data for each algorithm, especially Algorithm 7 which only has 13 patches in the training set! This is the single largest barrier I need to overcome to make the Algorithm 7 neural network accurate.
 
My current workflow for sample collection is a Deflemask (a multi-system chiptune tracker) music file consisting of a 4th octave C being played in the first FM channel for almost 1 second, a macro which imports a Y12 file into that channel and exports the "song" as a WAV file. The macro recorder I used is rather glitchy, and usually stops working after 7 or 8 iterations, so collecting enough samples to train a neural network will not be feasible with this method.

My proposed solution is to write a Genesis program that contains the entire patch collection I wish to use (I have around 5,600 patches) and plays a 4th octave C with each patch for about a second, one after the other (in Windows directory order, so I don't have to sort anything). After compiling the ROM, I can run it on a sound-accurate Genesis emulator (like Regen, for instance), while Audacity records the output. Then a simple Python loop can separate the (large) WAV file into individual files. My original motivation for this project was to use it to create instrument patches for Genesis homebrew projects, so I look forward to putting some of those 68K assembly programming skills I've learned to practice!