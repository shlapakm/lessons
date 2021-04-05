import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
D = [10,9,11,5,6,13,19,26]

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
    X=decToBinList(number%256)
    X.reverse()
    for i in range(8):
        GPIO.setup(D[i],GPIO.OUT)
    for i in range(8):
        GPIO.output(D[i],X[i])
    time.sleep(0.1)
def sinToVoltage(amplitude,samplingFrequency):
    for i in amplitude:
        value = int(i)
        X = decToBinList(value%256)
        X.reverse()
        for i in range(8):
            GPIO.setup(D[i],GPIO.OUT)
        for i in range(8):
            GPIO.output(D[i],X[i])
        time.sleep(1/samplingFrequency)

def sinToVoltage2(amplitude,samplingFrequency):
    for i in amplitude:
        value = int(i)
        X = decToBinList(value%256)
        X.reverse()
        for i in range(8):
            GPIO.setup(D[i],GPIO.OUT)
        GPIO.output(D,X)
        time.sleep(1/samplingFrequency)

try:
    #firstscript
    #print("Please, enter a number (if you want to exit the program, enter -1)")
    #decNumber = int(input())
    #while decNumber!=-1:
        #num2dac(decNumber)
        #print("Please, enter a number (if you want to exit the program, enter -1)")
        #decNumber = int(input())
    #secondscript
    #print("enter the number of repetitions")
    #repetitionsNumber = int(input())
    #decNumber=0
    #i=0
    #while i< repetitionsNumber:
        #for decNumber in range(256):
            #num2dac(decNumber)
        #for decNumber in range(255,0,-1):
            #num2dac(decNumber)
        #i+=1
    #thirdscript
    trrime = int(input())
    frequency = float(input())
    samplingFrequency = int(input())
    trime = np.arange(0, trrime, float(1/samplingFrequency))
    amplitude = (np.sin((2*3.14*frequency)*trime) +1)*127.5
    print(amplitude)
    sinToVoltage(amplitude,samplingFrequency)
    sinToVoltage2(amplitude,samplingFrequency)
    plt.plot(trime, amplitude)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()
finally:
    for i in range(8):
        GPIO.setup(D[i],GPIO.OUT)
    for i in range(8):
            GPIO.output(D[i],0)
