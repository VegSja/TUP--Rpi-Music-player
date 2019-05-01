import os
import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)

def checkButton():
    if(GPIO.input(10)):
        print("Ready to ROLL!")


def playSong():
    os.system("play Sang.wav")  
    time.sleep(7)
    os.system("echo 'finish'")

playSong()

        