import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
import librosa
import librosa.display


#import vlc
#import time

y,sr = librosa.load(r"/Users/dippaul/Downloads/SampleAudio_0.4mb.mp3")
#sound_file.play()

#time.sleep(10)

onset_env = librosa.onset.onset_strength(y, sr=sr)
tempo = librosa.beat.tempo(onset_env, sr=sr)

print("THE TEMPO (IN BPM) OF THE SAMPLE AUDIO FILE IS ")
print(*tempo)

