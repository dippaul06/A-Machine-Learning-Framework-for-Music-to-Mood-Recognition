#IMPORTING LIBRARIES
import librosa
import librosa.display
import IPython
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns

#LOADING THE AUDIO FILE
audio = r"/Users/dippaul/Desktop/MUSIC_FEATURE_EXTRACTION/MUSIC_SAMPLES/true.mp3"
y,sr=librosa.load(audio)

#AUDIO FEATURES
print('Audio Sampling Rate: '+str(sr)+' samples/sec')
print('Total Samples: '+str(np.size(y)))
secs=np.size(y)/sr
print('Audio Length: '+str(secs)+' s')

#Seperation of Harmonic and Percussive Signal
y_harmonic, y_percussive = librosa.effects.hpss(y)




###Tempo Extraction
tempo, beat_frames = librosa.beat.beat_track(y=y_harmonic, sr=sr)
print('Detected Tempo: '+str(tempo)+ ' beats/min')



###ZERO CROSSING FEATURE (WHERE THE SONG IS AT ZERO AMPLITUDE)
zrate=librosa.feature.zero_crossing_rate(y_harmonic)
zrate_mean=np.mean(zrate)
zrate_std=np.std(zrate)
zrate_skew=scipy.stats.skew(zrate,axis=1)[0]
print('ZCF Mean: '+str(zrate_mean))
print('ZCF SD: '+str(zrate_std))
print('ZCF Skewness: '+str(zrate_skew))



###MFCC
mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=5)
mfccs_mean=np.mean(mfccs,axis=1)
mfccs_std=np.std(mfccs,axis=1)
print('MFCC Mean: '+str(mfccs_mean))
print('MFCC Standard Deviation: '+str(mfccs_std))



###Chroma Energy Normalized (CENS)
chroma=librosa.feature.chroma_cens(y=y_harmonic, sr=sr)
chroma_mean=np.mean(chroma,axis=1)
chroma_std=np.std(chroma,axis=1)
print('CENS Mean: '+str(chroma_mean))
print('CENS Standard Deviation: '+str(chroma_std))




###SPECTRAL CENTROID (BRIGHTNESS OF THE SOUND)
cent = librosa.feature.spectral_centroid(y=y, sr=sr)
cent_mean=np.mean(cent)
cent_std=np.std(cent)
cent_skew=scipy.stats.skew(cent,axis=1)[0]
print('SC Mean: '+str(cent_mean))
print('SC Standard Deviation: '+str(cent_std))
print('SC Skewness: '+str(cent_skew))




###Spectral Contrast
contrast=librosa.feature.spectral_contrast(y=y_harmonic,sr=sr)
contrast_mean=np.mean(contrast,axis=1)
contrast_std=np.std(contrast,axis=1)
print('Mean: '+str(contrast_mean))
print('SD: '+str(contrast_std))




###Spectral Rolloff
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
rolloff_mean=np.mean(rolloff)
rolloff_std=np.std(rolloff)
rolloff_skew=scipy.stats.skew(rolloff,axis=1)[0]
print('Mean: '+str(rolloff_mean))
print('SD: '+str(rolloff_std))
print('Skewness: '+str(rolloff_skew))



####WRITING TO A CSV FILE
import csv

with open('/Users/dippaul/Desktop/test_csv.csv', mode='w' ) as csv_file:
    fieldnames = ['Tempo','ZCR Mean','ZCR Std Dev','MFCC Mean','MFCC Std Dev','CEN Mean','CEN Std Dev','CENTROID Mean','CENTROID Std Dev','Contrast Mean','Contrast Std Dev','Rolloff Mean','Rolloff Std Dev']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
##    writer = csv.writer(csv_file)
    writer.writeheader()
    writer.writerow({'Tempo': str(tempo),'ZCR Mean': str(zrate_mean),'ZCR Std Dev' : str(zrate_std),'MFCC Mean': str(mfccs_mean[0]),'MFCC Std Dev' : str(mfccs_std[0]),'CEN Mean' : str(chroma_mean[0]),'CEN Std Dev' : str(chroma_std[0]),'CENTROID Mean' : str(cent_mean),'CENTROID Std Dev' : str(cent_std),'Contrast Mean' : str(contrast_mean[0]),'Contrast Std Dev' : str(contrast_std[0]),'Rolloff Mean' : str(rolloff_mean),'Rolloff Std Dev' : str(rolloff_std)})



##    row = [str(tempo),str(zrate_mean),str(zrate_std),str(mfccs_mean[0]),str(mfccs_std[0]),str(chroma_mean[0]),str(chroma_std[0]),str(cent_mean),str(cent_std),str(contrast_mean[0]),str(contrast_std[0]),str(rolloff_mean),str(rolloff_std)]

    writer = csv.writer(csv_file)
##    writer.writerow(row)

    csv_file.close()
