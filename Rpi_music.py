import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def checkInput():
    print(GPIO.input(4))	
    if(GPIO.input(4)):
            playSong()
    else:
       print("Waiting for buttonpress")
       os.system("clear")
    time.sleep(1)
def playSong():
    os.system("play /etc/Musicplayer/Sang.wav")  
    os.system("echo 'finish'")

while True:
	checkInput()

        
