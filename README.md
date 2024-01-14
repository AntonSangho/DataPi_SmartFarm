# DataPi Smart Farm

# BOM   
|부품명|용도|위치|
|---|:---:|:---:|
|DS3231|Real Time IC|J11|
|DS18b20|방수 온도 센서|J5|
|AHT20|온습도 센서|J4|
|SSD1306|OLED 디스플레이|J10|
|WS2812b|네오픽셀(30개)|J7,J9|
|Buzzer|부저|BZ1|
|FAN|환풍기|J16|


# PinMap 
|설정|GPIO|연결|
|---|:-:|:---:|
|DIN1|2|우측네오픽셀|
|SW1|3|우측스위치|
|SDA|4|
|SCL|5|
|DI|6|방수온도센서|
|Buzz|7|부저|
|LED|9||
|SW2|14|좌측스위치|
|DIN2|15|좌측네오픽셀|
|FAN|26|환풍기|







# Reference 
- [websocket_using_microdot](https://www.youtube.com/watch?v=eSzrWhEBJgA)
- [Capture plant health with NDVI and Raspberry Pi](https://projects.raspberrypi.org/en/projects/astropi-ndvi/0)
- [Control a DC Fan with a Raspberry Pi](https://www.digikey.com/en/maker/projects/control-a-dc-fan-with-a-raspberry-pi/f3fa09ab84c049d08474b625bee8d8f2)
