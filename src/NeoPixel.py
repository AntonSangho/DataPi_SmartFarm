# Control 30 Neopixels in Pin 2 and 15 with micropython.

from machine import Pin
from neopixel import NeoPixel

#네오픽셀
np0 = NeoPixel(machine.Pin(2), 30)
np1 = NeoPixel(machine.Pin(15), 30)

def np_on():
    for i in range(0, np0.n):
        np0[i] = (250,250,250)
    for i in range(0, np1.n):
        np1[i] = (250,250,250)
    np0.write()
    np1.write()
def np_off():
    for i in range(0, np0.n):
        np0[i] = (0,0,0)
    for i in range(0, np1.n):
        np1[i] = (0,0,0)
    np0.write()
    np1.write()

np_state = "On"

while True:
    #np_on()
    np_off()
