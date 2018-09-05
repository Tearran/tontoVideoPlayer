#!/usr/bin/python

import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO
import os
import sys
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

thisState1 = thisState2 = thisState3 = 0
lastState1 = lastState2 = lastState3 = 0
playerState = 0

video1 = '/home/pi/Videos/movie1.mp4'
video2 = '/home/pi/Videos/movie1.mp4'
video3 = '/home/pi/Videos/movie1.mp4'

os.system('clear')
time.sleep(0.25)
os.system('reset')

splash = Popen(['fim', '/home/pi/Pictures/logo.png','-H','-q'])
#splash = os.system('fim', '/home/pi/Pictures/logo.png -H-q')
while True:
    thisState1 = 1 - GPIO.input(17)
    thisState2 = 1 - GPIO.input(27)
    thisState3 = 1 - GPIO.input(22)

    try:
        omxpState = subprocess.check_output('pgrep -l omxplayer.bin',shell=True)
        playerState = True
    except:
        playerState = False

    if thisState1 and not lastState1:
        if not playerState:
            Popen(['omxplayer', '-b', video1])
        elif playerState:
            os.system('killall omxplayer.bin')

    if thisState2 and not lastState2:
        if not playerState:
            Popen(['omxplayer', '-b', video1])
        elif playerState:
            os.system('killall omxplayer.bin') ,splash
			
    if thisState3 and not lastState3:
        if not playerState:
            Popen(['omxplayer', '-b', video1])
        elif playerState:
            os.system('killall omxplayer.bin')

    lastState1 = thisState1
    lastState2 = thisState2
    lastState3 = thisState3
    time.sleep(0.25)

