import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
D = [10,9,11,5,6,13,19,26]
GPIO.setup(D, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
#GPIO.output(D,1)
                
last=-3

GPIO.setup(17, GPIO.IN)
def decToBinList(decNumber):
    X = []
    N=7
    while N>=0:
        p = int(decNumber/(2**N))
        decNumber = decNumber - (p*(2**N))
        X.append(p)
        N-=1
    return X
def num2dac(number):
    X=decToBinList(number)
    X.reverse()
    GPIO.setup(D,GPIO.OUT)
    GPIO.output(D,X)
def adc_procedure(last):
    left=0
    right=255
    while right>left+1:
        middle = left+right
        middle=middle//2
        num2dac(middle) 
        if not GPIO.input(4):
            if abs(middle-last)>1:
                right=middle
                print(left,right)
        else:
            if abs(middle-last)>1:
                left=middle
                print(left,right)
    print('Digital value',left, 'Analog value: ','%.2fV' % float(3.3*left/255) )
    return left

try:
    GPIO.setup(4, GPIO.IN)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17,1)
    #while True:
        #value = int(input('Enter value (-1 to exit) '))
        #if value==-1:
            #exit()
        #num2dac(value)
        #print(value, '=', '%.2fV' % float(3.3*value/255))
    while True:
            last=adc_procedure(last)
            #adc_procedure()
        #print('Digital value ', adc_procedure(), 'Analog value ', '%.2fV' % float(3.3*value/255))
finally:
        GPIO.setup(D,GPIO.OUT)
        GPIO.output(D,0)