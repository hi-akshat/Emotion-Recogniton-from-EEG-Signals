# Emotion-Recogniton-from-DEAP

We used data from the DEAP dataset that has been pre-processed in MATLAB.

In this dataset, 32 subjects viewed 40 clips of video that could stimulate various emotions.

The length of each video is 60s.

Each subject provided a personal rating in the valence-arousal-dominance-liking four dimensions, ranging from 1 to 9, 1 is the smallest, and 9 is the largest.

During the pre-processing phase, a preparation time of 3 s was added to each video, thereby changing the total time
of each video to 63s.

We analyzed the emotion in the valence and arousal dimensions. If an individual’s score is greater than 4.5,
the level of arousal/valence is classified as high, whereas if the individual’s score is less than 4.5, the
level of arousal/valence is classified as low. 

We used the average mean reference (AMR)method to pre-process the EEG data. Then, toeliminate individual differences and channel differences, we normalized the EEG signals for each channel of each person to [0,1] using the min-max normalization method, thereby reducing the computational complexity. 

We used discrete wavelet transform (DWT) to extract EEG features. A series of wavelet coefficients were obtained by stretching and shifting the EEG signals using the mother wavelet function.

In our project, the window of 4 s was used for each EEG channel and each window overlaps the previous one by 2 s, for a total of 29 windows.

Then, the data of each window were decomposed 4 times by using db4 DWT and extracting all the high frequency components as four frequency bands, namely, gamma, beta, alpha and theta. 

Decomposition of EEG signal into different frequency bands using DWT

Frequency band Frequency range (Hz) Frequency bandwidth (Hz) Decomposition level

Theta          4–8                  4                        D4
Alpha          8–16                 8                        D3
Beta           16–32                16                       D2
Gamma          32–64                32                       D1

Finally,the entropy and energy of each frequency band were calculated as features. Thus, there are 2 features in
each band for each channel. There are 20 (2*10) features in 10 channels, and the numbers of features
are 28, 36 and 64 in 14, 18 and 32 channels, respectively.
