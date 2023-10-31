import time
from pygame import mixer


mixer.init()
mixer.music.load("./audio/1.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(0.1)
