from machine import Pin
import utime
from neopixel import NeoPixel

# 네오픽셀과 환풍기 핀 초기화
Rled = Pin(9, Pin.OUT)
Fan = machine.Pin(26, machine.Pin.OUT)
np0 = NeoPixel(machine.Pin(2), 30)
np1 = NeoPixel(machine.Pin(15), 30)
Rbutton = Pin(3, Pin.IN, Pin.PULL_UP)
Lbutton = Pin(14, Pin.IN, Pin.PULL_UP)

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
    print("Fan_state:", end =' ')
    print(Rbutton_state)
    Rled.value(Rbutton_state)
    Fan.value(Rbutton_state)

def Lbutton_handler(pin):
    global Lbutton_state
    # 버튼 상태 전환
    Lbutton_state = not Lbutton_state
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

while True:
    utime.sleep(0.1)
