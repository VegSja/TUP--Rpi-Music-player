import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def checkInput():
    print(GPIO.input(4))	
    if(GPIO.input(4)):
        print("Ready to ROLL!")
	playSong()
    else:
       print("Waiting for buttonpress")
       os.system("clear")

def playSong():
    os.system("play Sang.wav")  
    time.sleep(7)
    os.system("echo 'finish'")

while True:
	checkInput()

        
