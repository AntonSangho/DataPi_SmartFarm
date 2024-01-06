# Basic code for SSD1306 OLED display with Rasberry pi pico W in MicroPython 

from machine import Pin, I2C
import ssd1306

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.text("Hello World!", 0, 0)
oled.show()

#oled.fill(0)
#oled.show()



