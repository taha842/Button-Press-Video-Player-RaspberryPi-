# Engr.Muhammad Taha
# Github : taha842
# Facebook :  www.facebook.com/taha.munir.3

# 1st Step: You can install new operating system in Raspberry pi
# 2nd Step: Open Command Prompt and Install Follwoing Libraries (Just copy and paste followuing commands)
#           1. sudo apt install python3-gpiozero 
#           2. sudo apt-get update && sudo apt-get install -y libdbus-1{,-dev}
#           3. pip install omxplayer-wrapper
# 3rd Step: copy this file in your pi desktop and run this file  with python3.
# 4th Step: All 4 Video are rename with movie1, movie2, movie3, movie3 respectively
# 5th Step: Wiring example and pinout sheet mention in Pdf file.

from subprocess import Popen
from gpiozero import Button
from gpiozero import LED
from time import sleep
import os
import sys
from omxplayer.player import OMXPlayer
from pathlib import Path


button1 = Button(2)  # Button 1 Pin # 2
button2 = Button(3)  # Button 2 Pin # 3
button2 = Button(4)  # Button 3 Pin # 4
button2 = Button(17) # Button 4 Pin # 17

led1 = LED(14)       # Define Led 1 Pin # 14
led2 = LED(15)       # Define Led 2 Pin # 15
led3 = LED(18)       # Define Led 3 Pin # 18
led4 = LED(23)       # Define Led 4 Pin # 23

State1 = False       # Define State in true or false if player is in running condition it becomes true otherwise false
State2 = False       # Define State in true or false if player is in running condition it becomes true otherwise false
State3 = False       # Define State in true or false if player is in running condition it becomes true otherwise false
State4 = False       # Define State in true or false if player is in running condition it becomes true otherwise false


movie1 = Path("/home/pi/Desktop/movie1.mp4")  # Define movie Path( Current Location Desktop)
movie2 = Path("/home/pi/Desktop/movie2.mp4")  # Define movie Path( Current Location Desktop)
movie3 = Path("/home/pi/Desktop/movie3.mp4")  # Define movie Path( Current Location Desktop)
movie4 = Path("/home/pi/Desktop/movie4.mp4")  # Define movie Path( Current Location Desktop)

while(1):
    
    if button1.is_pressed and State1 == False:  # Play movie1 when button1 is press
        print("Movie 1 Playing")
        player = OMXPlayer(movie1)
        #os.system('killall omxplayer.bin')
        #omxc = Popen(['omxplayer', '-b', movie1])
        led1.on()
        State1 = True

        
    if button2.is_pressed and State2 == False:  # Play movie2 when button2 is press
        print("Movie 2 Playing")
        player = OMXPlayer(movie2)  
        #os.system('killall omxplayer.bin')
        #omxc = Popen(['omxplayer', '-b', movie2])
        led2.on()
        State2 = True
        
    if button3.is_pressed and State3 == False:  # Play movie3 when button3 is press
        print("Movie 3 Playing")
        player = OMXPlayer(movie3)
        #os.system('killall omxplayer.bin')
        #omxc = Popen(['omxplayer', '-b', movie3])
        led3.on()
        State3 = True
        
    if button4.is_pressed and State4 == False:  # Play movie4 when button4 is press
        print("Movie 4 Playing")
        player = OMXPlayer(movie4)
        #os.system('killall omxplayer.bin')
        #omxc = Popen(['omxplayer', '-b', movie4])
        led4.on()
        State4 = True
    
    
    if button1.is_pressed and State1 == True:   # Stop Movie when button is press again while playing video
        print("Movie 1 Stopped")
        player.quit()
        #os.system('killall omxplayer.bin')  
        led1.off()
        State1 = False
                
    if button2.is_pressed and State2 == True:   # Stop Movie when button is press again while playing video
        print("Movie 2 Stopped")
        player.quit()
        #os.system('killall omxplayer.bin')  
        led2.off()
        State2 = False
                
    if button3.is_pressed and State3 == True:   # Stop Movie when button is press again while playing video
        print("Movie 3 Stopped")
        player.quit()
        #os.system('killall omxplayer.bin')  
        led3.off()
        State3 = False
                
    if button4.is_pressed and State4 == True:   # Stop Movie when button is press again while playing video
        print("Movie 4 Stopped")
        player.quit()
        #os.system('killall omxplayer.bin')  
        led4.off()
        State4 = False
        
    if player.position() > (player.duration() - 0.2):
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        State1 = False
        State2 = False
        State3 = False
        State4 = False
        