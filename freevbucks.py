"""
# Free vbucks
# Edited by: Celvis
# Discord: Celvis#1772
# Original = https://github.com/stayfrostydoggo/Funny-Stuff-IG/blob/main/freevbucks.py
# Author = starfrostydoggo (Aka Bored)
"""

# Import Modules
import time
import os
import itertools
import threading
import sys

# Set vbux to 0
vbux = 0

# Wanted
wanted = int(input("How many vbucks do you want to receive: "))
vbux += wanted

# Fake load
# Load 1
load1 = False
def loader1():
    for c in itertools.cycle(['.', '..', '...','   ']):
        if load1:
            break
        sys.stdout.write("Loading vbucks" + c)
        sys.stdout.flush()
        time.sleep(3)
    t = threading.Thread(target=loader1)
    t.start()
# Process 1
load1 = True

# Load 2
load2 = False
def loader2():
    for c in itertools.cycle(['.', '..', '...','   ']):
        if load2:
            break
        sys.stdout.write("Breaching Fortnite mainframe" + c)
        sys.stdout.flush()
        time.sleep(5)
    t = threading.Thread(target=loader2)
    t.start()
# Process 2
load2 = True

# Load 3
load3 = False
def loader3():
    for c in itertools.cycle(['.', '..', '...','   ']):
        if load3:
            break
        sys.stdout.write("Bruteforcing vbux database" + c)
        sys.stdout.flush()
        time.sleep(4)
    t = threading.Thread(target=loader3)
    t.start()
# Process 3
load3 = True

# Load 4
load4 = False
def loader4():
    for c in itertools.cycle(['.', '..', '...','   ']):
        if load4:
            break
        sys.stdout.write("Siphoning vbux" + c)
        sys.stdout.flush()
        time.sleep(3)
    t = threading.Thread(target=loader4)
    t.start()
# Process 4
load4 = True

# Load 5
#print("Generating hash key for vbux...")
#time.sleep(3)





print("VBUS HAK COMPLETE!!1111!!1!")

print(f"you have {vbux} vbucks")
x = 0
time.sleep(2)


#while x < 100000:
print("OMG I LOVE FREE VBUX")
#        x += 1


#os.system("poweroff")