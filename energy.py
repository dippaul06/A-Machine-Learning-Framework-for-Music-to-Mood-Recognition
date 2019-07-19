import librosa


#y, sr = librosa.load(librosa.util.example_audio_file(("/Users/dippaul/Downloads/SampleAudio_0.4mb.mp3"))
#librosa.feature.rms(y=y)

y,sr = librosa.load(r"/Users/dippaul/Downloads/SampleAudio_0.4mb.mp3")
print(librosa.feature.rms(y=y))

