import vlc
import time

sound_file = vlc.MediaPlayer(r"/Users/dippaul/Downloads/SampleAudio_0.7mb.mp3")
sound_file.play()

time.sleep(10)
