import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)

def checkInput():
    if(GPIO.input(10)):
        print("Ready to ROLL!")
    else:
        print("Waiting for buttonpress")
        os.system("clear")

def playSong():
    os.system("play Sang.wav")  
    time.sleep(7)
    os.system("echo 'finish'")

while True:
	checkInput()

        
