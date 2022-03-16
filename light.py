#!/usr/bin/env python3

from yeelight import Bulb
import os

class Light():
    def __init__(self):
        bulb_ip = os.environ.get('BULB_IP')
        self.bulb = Bulb(bulb_ip)

    def busy(self):
        self.bulb.set_rgb(255, 0, 0)

    def available(self):
        self.bulb.set_rgb(139, 0, 255)
