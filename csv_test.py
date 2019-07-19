# importing the csv module
import csv
import librosa
import scipy
import pandas
import numpy as np
import  pandas as pd
from os import listdir
from os.path import isfile, join


def extract_feature(path):
    id = 1  # Song ID
    feature_set = pd.DataFrame()  # Feature Matrix

    # Individual Feature Vectors
    songname_vector = pd.Series()
    tempo_vector = pd.Series()
    mfcc_mean = pd.Series()
    mfcc_std = pd.Series()
    zcr_mean = pd.Series()
    zcr_std = pd.Series()

    # Traversing over each file in path
    file_data = [f for f in listdir(path) if isfile(join(path, f))]
    for line in file_data:
        if (line[-1:] == '\n'):
            line = line[:-1]

        # Reading Song
        songname = path + line
        y, sr = librosa.load(songname)



    # Reading Song
    #songname = path + line
    #y, sr = librosa.load(songname)
    #S = np.abs(librosa.stft(y))


    #y, sr = librosa.load(path)


        # Seperation of Harmonic and Percussive Signal
        y_harmonic, y_percussive = librosa.effects.hpss(y)

        ###Tempo Extraction
        tempo, beat_frames = librosa.beat.beat_track(y=y_harmonic, sr=sr)

        ###ZERO CROSSING FEATURE (WHERE THE SONG IS AT ZERO AMPLITUDE)
        zrate = librosa.feature.zero_crossing_rate(y_harmonic)
        zrate_mean = np.mean(zrate)
        zrate_std = np.std(zrate)

        ###MFCC
        mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=5)
        mfccs_mean = np.mean(mfccs, axis=1)
        mfccs_std = np.std(mfccs, axis=1)



        # Transforming Features

        tempo_vector.set_value(id, tempo)  # tempo
        mfcc_mean.set_value(id, np.mean(mfccs_mean))  # mfcc
        mfcc_std.set_value(id, np.std(mfccs_std))
        zcr_mean.set_value(id, np.mean(zrate_mean))  # zero crossing rate
        zcr_std.set_value(id, zrate_std)

  

        print(songname)
        id = id + 1

    # Concatenating Features into one csv and json format
    #feature_set['song_name'] = songname_vector  # song name
    feature_set['tempo'] = tempo_vector  # tempo
    feature_set['mfcc_mean'] = mfcc_mean  # mfcc
    feature_set['mfcc_std'] = mfcc_std

    feature_set['zcr_mean'] = zcr_mean  # zero crossing rate
    feature_set['zcr_std'] = zcr_std

    # Converting Dataframe into CSV Excel and JSON file
    feature_set.to_csv('Emotion_features.csv')


# Extracting Feature Function Call
extract_feature(r"/Users/dippaul/Desktop/MUSIC_FEATURE_EXTRACTION/MUSIC_SAMPLES/")





