from time import sleep
from pygame import mixer
mixer.init()

mixer.Channel(0).play(mixer.Sound("./sounds/Moai sound.mp3.mp3"))
mixer.Channel(1).play(mixer.Sound("./sounds/Emoji Scream.mp3"))
sleep(2.5)
