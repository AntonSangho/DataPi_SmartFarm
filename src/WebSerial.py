from machine import Pin, UART
import uos

led_pin = Pin("LED", Pin.OUT)  # Change the pin number to your board's LED pin
uart = UART(1, 9600)  # UART 1, and baud rate of 9600

def read_serial():
    if uart.any():  # Check if any data is available
        chr = uart.read(1)  # Read one byte
        if chr == b'H':
            led_pin.value(1)
        elif chr == b'L':
            led_pin.value(0)

while True:
    read_serial()