# -*- coding: utf-8 -*-

from libs.sh1106 import SH1106_I2C
from machine import Pin, SoftI2C
import time

i2c = SoftI2C(scl=Pin(16), sda=Pin(17))
oled = SH1106_I2C(128, 64, i2c)

OLED_WIDTH = 128
OLED_HEIGHT = 64

button = Pin(2, Pin.OUT)


def clean():
    pass


def show_bar(delay, start):
    """show progress bar"""

    oled.fill_rect(start[0], start[1], 4, 10, 1)

    step = delay // OLED_WIDTH
    step = step if step > 1 else 1

    for _ in range(OLED_WIDTH):
        oled.scroll(1, 0)
        time.sleep(step)
        oled.show()


while True:

    show_bar(60, [0, 0])
