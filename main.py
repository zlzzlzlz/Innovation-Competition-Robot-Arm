import os
import time
import tkinter


def huataiheng(距离,方向):
    juli = 0
    xiang = 0
    juli = 距离
    xiang = 方向
    import RPi.GPIO as GPIO
    import time
    # juli = juli / 125
    # juli = juli * 1600
    # juli = juli / 4000
    # juli = juli * 3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(10,GPIO.OUT)
    if xiang == 1:
        GPIO.output(10,GPIO.HIGH)
    else:
        GPIO.output(10,GPIO.LOW)
    GPIO.setup(22,GPIO.OUT)
    pwm = GPIO.PWM(22, 4000)
    pwm.start(50)
    time.sleep(juli)
    pwm.stop()

def huataishu(距离, 方向):
    import RPi.GPIO as GPIO
    import time
    # 距离 = 距离 / 125
    # 距离 = 距离 * 1600
    # 距离 = 距离 / 4000
    # 距离 = 距离 * 6
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    if 方向 == 0:
        GPIO.output(27,GPIO.HIGH)
        print("1")
    else:
        GPIO.output(27,GPIO.LOW)
    GPIO.setup(25,GPIO.OUT)
    pwm = GPIO.PWM(25, 4000)
    pwm.start(50)
    time.sleep(距离)
    pwm.stop()
    GPIO.cleanup()

def xi(timee):
    import  RPi.GPIO as GPIO
    import time
    print("run")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3,GPIO.OUT)
    pwm = GPIO.PWM(3,400)
    pwm.start(95)
    print("runing")
    time.sleep(timee)
    print("sleepOK")
    pwm.stop()
    GPIO.cleanup()
    print("runOK")

def fang():
    import  RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.OUT)
    pwm = GPIO.PWM(21,400)
    pwm.start(95)
    time.sleep(3)
    pwm.stop()
    GPIO.cleanup()


def ceju():
    import RPi.GPIO as GPIO
    GPIO_TRIG = 20
    GPIO_ECHO = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIG, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    # 发送高电平信号到 Trig 引脚
    GPIO.output(GPIO_TRIG, 1)
    # 持续 10 us
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, 0)

    # 高电平持续时间就是超声波从发射到返回的时间
    while GPIO.input(GPIO_ECHO) == GPIO.LOW:
        pass
        # print("bb")
    start_time = time.time()
    while GPIO.input(GPIO_ECHO) == GPIO.HIGH:
        pass
        # print("aa")
    stop_time = time.time()
    print("hahaha")

    # 计算距离 声波的速度为 34000cm/s。
    distance = ((stop_time - start_time) * 34000) / 2

    return distance


def xiufu():
    huataishu(4.5, 0)
    huataiheng(23, 0)
    huataishu(0.7, 1)
    xi(2.5)
    huataishu(1.93, 0)
    huataiheng(6.5, 0)
    fang()
    huataishu(1, 0)

    huataiheng(15, 1)
    huataishu(6.2, 1)
    xi(3)
    huataishu(1, 0)
    huataiheng(3, 1)
    huataishu(3.5, 0)
    xi(0.7)
    huataishu(3, 0)
    xi(2)
    huataiheng(6, 0)
    xi(1)
    huataiheng(5, 0)
    xi(1)
    huataiheng(5, 0)
    xi(1)
    huataiheng(6, 0)
    huataishu(0.6, 1)
    fang()


# ----------------------------------------------
# ----------------------------------------------


while True:
    juli = (ceju() + ceju() + ceju() + ceju() + ceju()) / 5
    print(juli)
    if juli < 30:
        os.system("espeak -a 200 -v zh 检测中")
        time.sleep(3)
        os.system("espeak -a 200 -v zh 这个艺术品不太美，让我来改造一下。")
        xiufu()
        os.system("espeak -v zh 这才是最完美的艺术品，比原来的形状对称美观多了！")
        exit(0)
    elif juli < 100:
        time.sleep(3)
        juli = (ceju() + ceju() + ceju() + ceju() + ceju()) / 5
        if juli < 30:
            continue
        os.system("espeak -v zh 检测中")
        time.sleep(3)
        os.system("espeak -v zh 这个艺术品是美的，不用改造。")

    time.sleep(1)



