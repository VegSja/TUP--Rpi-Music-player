import os
import RPi.GPIO as GPIO
import time
import random

#Setter opp GPIO pins på Raspberry Pi brettet
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Setter opp slik at pin 4 krever en lavere spenning for å aktiveres

#Deklarerer filplasseringen til de forskjellige sangene i en array
songs = ["/etc/Musicplayer/blind.wav", "/etc/Musicplayer/stal.wav", "/etc/Musicplayer/subwoofer.wav", "/etc/Musicplayer/wait", "/etc/Musicplayer/wet"]

def checkInput():
    print(GPIO.input(4)) 
    #Sjekker om knappen er trykket ned
    if(GPIO.input(4)):
            playSong() 
    else:
       print("Waiting for buttonpress")
       os.system("clear")
    time.sleep(1)
#Velger sang tilfeldig
def playSong():
    songNumber = random.randint(0,5) #Generer tilfedig tall mellom 0 og 5
    os.system("play" + songs[songNumber]) #Velger sang fra tidligere array basert på tallet songNumber og bruker kommandoen play for å spille sangen.
    os.system("echo 'finish'") #Skriver finish når er ferdig.

while True:
	checkInput() #Kjører checkInput hele tiden når koden kjører

        
