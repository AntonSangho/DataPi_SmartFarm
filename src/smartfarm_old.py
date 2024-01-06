##weekend test
from machine import Pin, PWM
from utime import time, sleep
from neopixel import NeoPixel

#네오픽셀
np0 = NeoPixel(machine.Pin(0), 30)
np1 = NeoPixel(machine.Pin(1), 30)

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
np_state = "On"
first = True

#환풍기1
motor_l1 = PWM(Pin(2))
motor_r1 = PWM(Pin(3))
motor_l1.freq(100)  # Hz단위로, 1초에 몇번 전류를 보내지 설정
motor_r1.freq(100)  # 높을수록 초당 연산은 많아지고, 제어는 부드러워짐
#환풍기2
motor_l2 = PWM(Pin(4))
motor_r2 = PWM(Pin(5))
motor_l2.freq(100)  # Hz단위로, 1초에 몇번 전류를 보내지 설정
motor_r2.freq(100)  # 높을수록 초당 연산은 많아지고, 제어는 부드러워짐


# 시간 설정
start_time = time()
prev_time_sensor = time()
start_time_np = time()
prev_time_np = time()

while True:    
    #시간
    current_time = time()
    elapsed_seconds = int(current_time - start_time)
    # 1초마다 OLED상태 업데이트
    if current_time - prev_time_sensor >= 1:
        prev_time_sensor = time()
        print(elapsed_seconds, np_state, first)
        
    #환풍기1 항시 가동
    motor_l1.duty_u16(10000)	# 0~65535 사이 값으로 속도 제어
    motor_r1.duty_u16(0)		# 여기는 0으로 유지
    #환풍기2 항시 가동
    motor_l2.duty_u16(10000)	# 0~65535 사이 값으로 속도 제어
    motor_r2.duty_u16(0)		# 여기는 0으로 유지
    
    # 네오픽셀 18시간 켜고 6시간 끄기
    if first:
        np_state = "On"
        np_on()
        if current_time - start_time >= 7*3600:
            prev_time_np = time()
            first = False
            np_state = "Off"
            np_off()
    else:
        if np_state == "Off":
            if current_time - prev_time_np >= 6*3600 : 
                np_state = "On"
                np_on()
                prev_time_np = time()

        if np_state == "On": 
            if current_time - prev_time_np >= 18*3600 :
                np_state = "Off"
                np_off()
                prev_time_np = time()


