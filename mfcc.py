import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
import librosa
import librosa.display



y,sr = librosa.load(r"/Users/dippaul/Downloads/SampleAudio_0.4mb.mp3")

mf = librosa.feature.mfcc(y, sr=sr)
print(*mf)