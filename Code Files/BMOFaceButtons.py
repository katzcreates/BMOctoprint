from gpiozero import Button #Much easier way to interact with the GPIO
from omxplayer import OMXPlayer
from pathlib import Path
import time
from signal import pause
import os
import subprocess

button_right = Button(6) 
button_up = Button(16)
button_left = Button (5)
button_down = Button (25)

def video_right():
    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-F", "/home/pi/BMO/BMO_Idle.jpg"])
    time.sleep(0.1)
    os.system("xscreensaver-command -deactivate")
    time.sleep(0.1)
    VIDEO_PATH = Path("/home/pi/BMO/BMO_DontSayThings_ColorAdjust.mp4")
    player = OMXPlayer(VIDEO_PATH, args=['-o', 'alsa'])
    player.set_aspect_mode('stretch')
    player.set_rate(0.975)
    time.sleep(4.7)
    os.system("xscreensaver-command -activate")
    image.kill()
    
    
def video_up():
    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-F", "/home/pi/BMO/BMO_Idle.jpg"])
    time.sleep(0.1)
    os.system("xscreensaver-command -deactivate")
    time.sleep(0.1)
    VIDEO_PATH = Path("/home/pi/BMO/BMO_WorryBaby_ColorAdjust.mp4")
    player = OMXPlayer(VIDEO_PATH, args=['-o', 'alsa'])
    player.set_aspect_mode('stretch')
    player.set_rate(0.975)
    time.sleep(3.5)
    os.system("xscreensaver-command -activate")
    image.kill()
    
def video_down():
    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-F", "/home/pi/BMO/BMO_Idle.jpg"])
    time.sleep(0.1)
    os.system("xscreensaver-command -deactivate")
    time.sleep(0.1)
    VIDEO_PATH = Path("/home/pi/BMO/BMO_YourHand_ColorAdjust.mp4")
    player = OMXPlayer(VIDEO_PATH, args=['-o', 'alsa'])
    player.set_aspect_mode('stretch')
    player.set_rate(0.975)
    time.sleep(4)
    os.system("xscreensaver-command -activate")
    image.kill()
    
def video_left():
    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-F", "/home/pi/BMO/BMO_Idle.jpg"])
    time.sleep(0.1)
    os.system("xscreensaver-command -deactivate")
    time.sleep(0.1)
    VIDEO_PATH = Path("/home/pi/BMO/BMO_WelcomeFriends_ColorAdjust.mp4")
    player = OMXPlayer(VIDEO_PATH, args=['-o', 'alsa'])
    player.set_aspect_mode('stretch')
    player.set_rate(0.975)
    time.sleep(6)
    os.system("xscreensaver-command -activate")
    image.kill()
    
    
button_right.when_pressed = video_right
button_up.when_pressed = video_up
button_down.when_pressed = video_down
button_left.when_pressed = video_left

pause()


