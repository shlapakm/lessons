import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
D = [24,25,8,7,12,16,20,21]
def lightUp(ledNumber,period):
    GPIO.setup(D[ledNumber], GPIO.OUT)
    GPIO.output(D[ledNumber],1)
    time.sleep(period)
    GPIO.output(D[ledNumber],0)
def blink(ledNumber, blinkCount, blinkPeriod):
    GPIO.setup(D[ledNumber], GPIO.OUT)
    for i in range(blinkCount):
        GPIO.output(D[ledNumber],1)
        time.sleep(blinkPeriod)
        GPIO.output(D[ledNumber],0)
        time.sleep(blinkPeriod)
def runningLight(count,period):
    for i in range(count):
        for j in range(8):
            GPIO.setup(D[j], GPIO.OUT)
            GPIO.output(D[j],1)
            time.sleep(period)
            GPIO.output(D[j],0)
            #time.sleep(period)
def runningDark(count,period):
     for i in range(count):
        for j in range(8):
            GPIO.setup(D[j], GPIO.OUT)
            GPIO.output(D[j],1)
        for j in range(8):
            GPIO.output(D[j],0)
            time.sleep(period)
            GPIO.output(D[j],1)
            #time.sleep(period)   
        for k in range(8):
            GPIO.output(D[k],0)
def decToBinList(decNumber):
    X = []
    N=7
    while N>=0:
        p = int(decNumber/(2**N))
        decNumber = decNumber - (p*(2**N))
        X.append(p)
        N-=1
    
    return X
def lightNumber(number):
    X=decToBinList(number)
    X.reverse()
    for i in range(8):
        GPIO.setup(D[i],GPIO.OUT)
    for i in range(8):
        if X[i]==1:
            GPIO.output(D[i],1)
    time.sleep(5)
    for i in range(8):
        GPIO.output(D[i],0)
def runningPattern(pattern,direction):
    X=decToBinList(pattern)
    if direction==1:
        i=7
        nol=X[7]
        while i>0:
            X[i]=X[i-1]
            i-=1
        X[0]=nol
    else:
        i=0
        nol = X[0]
        while i<7:
            X[i]=X[i+1]
            i+=1
        X[7]=nol
    X.reverse()
    for i in range(8):
        GPIO.setup(D[i],GPIO.OUT)
    for i in range(8):
        if X[i]==1:
            GPIO.output(D[i],1)
    time.sleep(5)
    for i in range(8):
        GPIO.output(D[i],0)


#ledNumber = int(input())
#blinkCount = int(input())
#blinkPeriod = float(input())
#count = int(input())
#period = float(input())
#lightUp(ledNumber, period)
#blink(ledNumber, blinkCount, blinkPeriod)
#runningLight(count,period)
#runningDark(count,period)
decNumber = int(input())
#direction=int(input())
#print(decToBinList(decNumber))
#number = int(input())
if decNumber<=255:
    lightNumber(decNumber)
    #runningPattern(decNumber,direction)
else:
    print("Error")
