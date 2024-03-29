# I2C Scan으로 부품의 이상유무를 확인할 수 있다

import machine

sdaPIN=machine.Pin(4)
sclPIN=machine.Pin(5)

i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)

devices = i2c.scan()
if len(devices) != 0:
    print('Number of I2C devices found=',len(devices))
    for device in devices:
        print("Device Hexadecimel Address= ",hex(device))
        if device == 0x3c:
            print("OLED Display")
        elif device == 0x68:
            print("Real Time Clock")
        else:
            print("Unknown Device")
else:
    print("No device found")