# websocket_server.py
import machine
import utime
import uwebsocket
import network
import ahtx0
from src.mywifi import networksetting

# Connect to WiFi
def connect_to_wifi():
    ssid, password = networksetting()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        utime.sleep(1)

    print("Connected to WiFi:", ssid)
    print("IP Address:", wlan.ifconfig()[0])

connect_to_wifi()

I2C_SDA_PIN = 4
I2C_SCL_PIN = 5

i2c = machine.I2C(0, sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)
sensor = ahtx0.AHT20(i2c)

# WebSocket handler function
def websocket_handler(socket, addr, data):
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    response = f'Temperature: {temperature:.2f} C, Humidity: {humidity:.2f} %'
    socket.send(response)

# Create a WebSocket server
ws_server = uwebsocket.WebSocketServer(handler=websocket_handler)

# Start the WebSocket server on port 8080
ws_server.run(port=8080)


