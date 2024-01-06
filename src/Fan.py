# Fan control with GPIO pin26 with 2N3904 NPN transistor in Micropython

import machine
import utime

# Pin 26 set to output
fan = machine.Pin(26, machine.Pin.OUT)

# fan on and off with while loop 

while True:
    #fan.on()
    #utime.sleep(5)
    fan.off()
    #utime.sleep(0)



