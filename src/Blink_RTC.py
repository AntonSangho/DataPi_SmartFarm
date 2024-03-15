from machine import Pin # Import Pin library
import utime # Import utime library
from machine import RTC
from machine import SoftI2C
import ssd1306

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

led = Pin("LED", Pin.OUT)  
rtc = RTC()

while True: # Loop forever
    oled.fill(0)
    current_time = rtc.datetime()
    # 특정 시간에 LED를 켜고 끄기 위한 코드
    print(current_time[6])
    if current_time[6] % 4 == 0:
        led.value(1)
        oled.text("LED ON", 0, 0)
        oled.show()
        utime.sleep(1)
    else:
        oled.fill(0)
        led.value(0)
        oled.text("LED OFF", 0, 0)
        oled.show()
        utime.sleep(1)
    utime.sleep(1) # Sleep for 1 second

