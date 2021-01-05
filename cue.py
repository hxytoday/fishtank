from machine import Pin, PWM
import time

LeTea4=[262,294,330,349,392,440,494]
LeTea5=[523,587,659,698,784,880,988]
LeTea6=[1047,1175,1319,1397,1568,1760,1976,2093,2349,2637,2794,3136,3520,3951,4186]
SongXxx=[1,350,1,350,5,350,5,350,6,350,6,350,5,700,4,350,4,350,3,350,3,350,2,350,2,350,1,700,5,350,5,350,4,350,4,350,3,350,3,350,2,700,5,350,5,350,4,350,4,350,3,350,3,350,2,700,1,350,1,350,5,350,5,350,6,350,6,350,5,700,4,350,4,350,3,350,3,350,2,350,2,350,1,700]
SongDh=[3,400,5,400,6,400,6,800,6,400,6,800,7,400,6,400,5,400,5,800,6,400,5,800,3,400,2,400,1,400,1,800,1,400,1,800,2,800,3,2400]

def lamp(mode):

    i = 0
    l = Pin(2, Pin.OUT)
    if mode == 'off':
        l.value(0)
    elif mode == 'on':
        l.value(1)
    elif mode > 1 and mode < 100:
        for i in range(0, mode):
            l.value(1)
            time.sleep_ms(200)
            l.value(0)
            time.sleep_ms(200)
    else:
        l.value(1)
        time.sleep_ms(mode)
        l.value(0)


def beep(freq,delay):
    Beep = PWM(Pin(25), freq=0, duty=512)
    Beep.freq(freq)
    time.sleep_ms(delay)
    Beep.deinit()

def music(song):
    if song=='Xxx':
        Song=SongXxx
    elif song=='Dh':
        Song=SongDh
    for index in range(0,len(Song),2):
        beep(LeTea6[Song[index]-1],Song[index+1])
