from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
#from ldr_photoresistor_module import LDR
#from ldr_photoresistor_module import DS18X20 
import time
import machine, onewire, ds18x20, time
from machine import I2C, Pin
from ds3231_port import DS3231
import ahtx0

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
        await ws.send(str(aht20.temperature))
        #await ws.send(str(aht20.relative_humidity))
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
