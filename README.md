# SampleToYM2612
 ML model for predicting the main register settings for a single patch for the Yamaha YM2612 FM synthesis sound chip used in the Sega Genesis/Mega Drive. To be precise, it will be expected to predict the register settings for...
 1) the algorithm used (out of 8 possibilities ranging from simple 4-way additive synthesis to a single chain of 1 carrier and 3 modulators),
 2) the ratios of all operator frequencies to the fundamental frequency (determined by the note being played), and
 3) the amplitudes of the sine wave operators used.
 
 It bases its prediction on the spectrum of an audio sample. The model will be trained using the spectra (features) and the aforementioned chip registers (targets) of samples taken from the output of a Sega Genesis.

 Comment about the scope of this project: the YM2612 chip has several more registers for each operator, including attack, decay, and sustain. These three (and hopefully some others) will come in a later version, and will likely involve the full sample as training data, not just the spectra. For now, I'll be happy to accomplish what I've promised above, as it forms the core essence of the sound.
 
 A related comment: the registers regarding release for each operator will be the most difficult to predict, because my training set will not only involve patch samples and register settings, but exact timestamps for when each sampled note is "released," since an FM synthesizer can allow the note to continue playing for a short time after the key is released, and moreover, operators can fade faster or slower than others, allowing a warping of the sound as it fades. I need to think of a streamlined approach to gathering the training data for this.