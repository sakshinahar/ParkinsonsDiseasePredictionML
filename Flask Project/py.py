import pandas as pd
from pyAudioAnalysis import audioBasicIO
def stereo_to_mono(signal):
    """
    This function converts the input signal
    (stored in a numpy array) to MONO (if it is STEREO)
    """

    if signal.ndim == 2:
        if signal.shape[1] == 1:
            signal = signal.flatten()
        else:
            if signal.shape[1] == 2:
                signal = (signal[:, 1] / 2) + (signal[:, 0] / 2)
    return signal
from pyAudioAnalysis import ShortTermFeatures
audio_file = "C:/Users/sradi/Downloads/Recording.mp3"

# Load the audio file using the audioBasicIO library
[Fs, x] = audioBasicIO.read_audio_file(audio_file)
x =stereo_to_mono(x)
# Extract the features using the audioFeatureExtraction library

#import matplotlib.pyplot as plt
#[Fs, x] = audioBasicIO.read_audio_file("sample.wav")
F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.050*Fs, 0.050*Fs)
#plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[0]) 
#plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel(f_names[1]); plt.show()
#[F, f_names] = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)

# Extract the specific features you're interested in
features_dict = {'MDVP:Fo(Hz)': F[0], 'MDVP:Fhi(Hz)': max(F[1]), 'MDVP:Flo(Hz)': min(F[1]), 
                'MDVP:Jitter(%)': F[8], 'MDVP:Jitter(Abs)': F[9], 'MDVP:RAP': F[10], 'MDVP:PPQ': F[11], 
                'Jitter:DDP': F[12], 'MDVP:Shimmer': F[13], 'MDVP:Shimmer(dB)': F[14], 'Shimmer:APQ3': F[15], 
                'Shimmer:APQ5': F[16], 'MDVP:APQ': F[17], 'Shimmer:DDA': F[18], 'NHR': F[19], 'HNR': F[20], 
                'RPDE': F[21], 'D2': F[22], 'DFA': F[23], 'spread1': F[24], 'spread2': F[25], 'PPE': F[26]}
new = pd.DataFrame.from_dict(features_dict)
print(new.head())

