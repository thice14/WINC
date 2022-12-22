# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

#1:
from readline import set_completion_display_matches_hook
import this

#2:
import time

def wait(seconds):
    time.sleep(seconds)
    return

#3:
import math

def my_sin(number):
    sine = math.sin(float(number))
    return sine

#4:
from datetime import datetime as dt

def iso_now():
    now = dt.now()
    now_string = now.strftime("%Y-%m-%dT%H:%M")
    return now_string

#5:
import sys

def platform():
    platform = sys.platform
    return platform

#6:
import greet

def supergreeting_wrapper(name):
    sg_wrapper = greet.supergreeting(name)
    return sg_wrapper

if (__name__ == '__main__'):
    print(iso_now())
    print(platform())
    print(supergreeting_wrapper('Thijs'))



