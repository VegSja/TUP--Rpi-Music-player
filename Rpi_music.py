import os
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

songs = ["/etc/Musicplayer/Sang.wav", "/etc/Musicplayer/TNT.wav", "/etc/Musicplayer/Minecraft_Style.wav"]

def checkInput():
    print(GPIO.input(4))	
    if(GPIO.input(4)):
            playSong()
    else:
       print("Waiting for buttonpress")
       os.system("clear")
    time.sleep(1)
def playSong():
    songNumber = random.randint(0,2)
    os.system("play" + songs[songNumber])  
    os.system("echo 'finish'")

while True:
	checkInput()

        
