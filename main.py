from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
#from ldr_photoresistor_module import LDR
#from ldr_photoresistor_module import DS18X20 
import time
import machine, onewire, ds18x20, time
from machine import I2C, Pin, SoftI2C
from ds3231_port import DS3231
import ahtx0
import ssd1306
from neopixel import NeoPixel

# 네오픽셀과 환풍기 핀 초기화
Rled = Pin(9, Pin.OUT)
Fan = machine.Pin(26, machine.Pin.OUT)
np0 = NeoPixel(machine.Pin(2), 30)
np1 = NeoPixel(machine.Pin(15), 30)
Rbutton = Pin(3, Pin.IN, Pin.PULL_UP)
Lbutton = Pin(14, Pin.IN, Pin.PULL_UP)

#OLED 초기화
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# I2C에 연결된 DS3231 초기화
ds3231 = DS3231(i2c) 
print('DS3231 time:', ds3231.get_time())

# 버튼 상태를 추적하는 변수 초기화
Rbutton_state = False
Lbutton_state = False

# 네오픽셀 상태를 추적하는 변수 초기화 
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

# 버튼이 눌렸을 때 호출될 핸들러 함수 정의
def Rbutton_handler(pin):
    global Rbutton_state
    # 버튼 상태 전환
    Rbutton_state = not Rbutton_state
    #if Rbutton_state == True:
        #oled.fill(0)
        #oled.show()
        #oled.text('Fan On', 0, 10)
        #oled.show()
    #else:
        #oled.fill(0)
        #oled.show()
        #oled.text('Fan Off', 0, 10)
        #oled.show()
        
    print("Fan_state:", end =' ')
    print(Rbutton_state)
    Rled.value(Rbutton_state)
    Fan.value(Rbutton_state)

def Lbutton_handler(pin):
    global Lbutton_state
    # 버튼 상태 전환
    Lbutton_state = not Lbutton_state
    #if Lbutton_state == True:
        #oled.fill(0)
        #oled.show()
        #oled.text('Neopixel On', 0, 10)
        #oled.show()
    #else:
        #oled.fill(0)
        #oled.show()
        #oled.text('Neopixel Off', 0, 10)
        #oled.show()
    print("Neopixel_state:", end =' ' )
    print(Lbutton_state)
    # np_on or np off
    if Lbutton_state == True:
        np_on()
    else:
        np_off()

# 버튼에 핸들러 등록
Rbutton.irq(trigger=Pin.IRQ_FALLING, handler=Rbutton_handler)
Lbutton.irq(trigger=Pin.IRQ_FALLING, handler=Lbutton_handler)

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'

# LDR module
#ldr = LDR(27)

# DS18B20 module pin 6
#ds_pin = machine.Pin(6)
#ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
#roms = ds_sensor.scan() 

# Connect to DS3231
sdaPIN = Pin(4) # SDA pin
sclPIN = Pin(5) # SCL pin
i2c = I2C(0, sda=sdaPIN, scl=sclPIN) # Init I2C using pins sda and scl
ds3231 = DS3231(i2c) # Create DS3231 object

# Initialize AHT20
aht20 = ahtx0.AHT20(i2c)

# root route
@app.route('/')
async def index(request):
    return render_template('index.html')

@app.route('/ws')
@with_websocket
async def read_sensor(request, ws):
    while True:
        #ds_sensor.convert_temp()
#         data = await ws.receive()
        time.sleep(.1)
        #time.sleep_ms(750)
        #await ws.send(str(ldr.get_light_percentage()))
        #await ws.send(str(ds_sensor.read_temp(roms[0])))
        #await ws.send(str(aht20.temperature))
        await ws.send(str(aht20.relative_humidity))
        #await ws.send(f"DS18B20 Temp: {str}, AHT20 Temp: {aht20.temperature}, AHT20 Humidity: {aht20.relative_humidity}")


# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)


# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass
