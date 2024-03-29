# boot.py -- run on boot-up
import network

# Replace the following with your WIFI Credentials
#SSID = "tresc3-2.4G"
#SSI_PASSWORD = "tresc333"

#SSID = "showme_2.4G"
#SSI_PASSWORD = "sangho1028"

#SSID = "anton"
#SSI_PASSWORD = "sangho1028"

SSID = "5G100_2G_000EBE"
SSI_PASSWORD = "#234567!"


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()
