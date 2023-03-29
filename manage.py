#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import _thread
from imu.IMU import run

import RPi.GPIO as GPIO
from commmunicate import message

INT_GPIO = 17

def button_pressed(channel):  
    print("falling edge detected on 17")
    message.send_message(message="stop")
    

def loop():
    """ Function to handle the interruptions of hardware and make the measurement of the MPU 6050
    """
    
    thread = _thread.start_new_thread(run, (3, 0x68)) # create a new thread to make the measurement of the MPU 6050 and send vy serial to the arduino
    

def main():
    GPIO.setmode(GPIO.BCM) # the numer's of the pins correspond to the chip BROADCOM

    # GPIO 17 set up as input, pulled up to avoid false detection.  
    # this port is wired to connect to GND on button press.  
    # So we'll be setting up falling edge detection 
    GPIO.setup(INT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
    GPIO.add_event_detect(INT_GPIO, GPIO.FALLING, callback=button_pressed, bouncetime=600)  
  
    
    try:
        #thread = _thread.start_new_thread(run, (3, 0x68)) # create a new thread to make the measurement of the MPU 6050 and send vy serial to the arduino
        thread = _thread.start_new_thread(loop,()) # loop 
    except Exception as e:
        print(e)     
        
    
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot_control.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
