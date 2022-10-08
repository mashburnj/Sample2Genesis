# SampleToYM2612
 ML model for predicting the main register settings for a single patch for the Yamaha YM2612 FM synthesis sound chip used in the Sega Genesis/Mega Drive. To be precise, it will be expected to predict the register settings for...
 1) the algorithm used (out of 8 possibilities ranging from simple 4-way additive synthesis to a single chain of 1 carrier and 3 modulators),
 2) the ratios of all operator frequencies to the fundamental frequency (determined by the note being played), and
 3) the amplitudes of the sine wave operators used.
 
 It bases its prediction on the spectrum of an audio sample. The model will be trained using the spectra (features) and the aforementioned chip registers (targets) of samples taken from the output of a Sega Genesis.

 Comment about the scope of this project: the YM2612 chip has several more registers for each operator, including attack, decay, and sustain. These three (and hopefully some others) will come in a later version, and will likely involve the full sample as training data, not just the spectra. For now, I'll be happy to accomplish what I've promised above, as it forms the core essence of the sound.
 
 A related comment: the registers regarding release for each operator will be the most difficult to predict, because my training set will not only involve patch samples and register settings, but exact timestamps for when each sampled note is "released," since an FM synthesizer can allow the note to continue playing for a short time after the key is released, and moreover, operators can fade faster or slower than others, allowing a warping of the sound as it fades. I need to think of a streamlined approach to gathering the training data for this.
 
 
 Done so far:
 - Spectrum analyzer, with a loop version which stores all spectra in a single CSV (DataFrame, with wav file names as indices)
 - A WAV to CSV script, which compiles the raw audio data into a CSV (I plan to use dimension reduction on this- we'll see how that goes)
 - A Y12 to CSV script, which interprets the bytes in each instrument file and organizes the information in a CSV (another DataFrame)
 
 To do:
 - Fix a small bug in the Y12 script.
 - The ML training scripts. Will need one model for each of the 8 FM algorithms.
 - The ML prediction script. Has to be able to extract the raw audio and its spectrum, then give 8 different predictions, and compare. I'm still undecided on which metric to use to compare (L2 on the spectra, perhaps?).
 
 In the future:
 - Take more sophisticated samples, with a common time to release the "key" to observe the release behavior.
 - Switch from Deflemask to a custom Genesis ROM which will play all instruments in the training set one after the other, while Audacity records the output (either through Regen or a Genesis).
 - Find a FM synthesis library for Python so I can generate audio based on the predictions and compare either the spectra, raw audio output, or both.