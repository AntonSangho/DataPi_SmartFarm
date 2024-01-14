from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
#from ldr_photoresistor_module import LDR
#from ldr_photoresistor_module import DS18X20 
import time
import machine, onewire, ds18x20, time

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'

# LDR module
#ldr = LDR(27)

# DS18B20 module pin 6
ds_pin = machine.Pin(6)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan() 
print('Found DS devices: ', roms)
ds_sensor.convert_temp()


# root route
@app.route('/')
async def index(request):
    return render_template('index.html')


@app.route('/ws')
@with_websocket
async def read_sensor(request, ws):
    while True:
#         data = await ws.receive()
        time.sleep(.1)
        #await ws.send(str(ldr.get_light_percentage()))
        await ws.send(str(ds_sensor.read_temp(roms[0])))

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
