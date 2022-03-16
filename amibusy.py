#!/usr/bin/env python3

import schedule
import time
import os, subprocess
from light import Light

l = Light()

def job():
    filename = "/dev/video0"
    busy = True
    try:
        pids = subprocess.check_output(['fuser', filename])
    except subprocess.CalledProcessError:
        busy = False
    if busy:
        print("Busy")
        l.busy()
    else:
        print("Not Busy!")
        l.available()

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
