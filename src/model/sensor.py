import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(38, gpio.OUT) #trigger
    gpio.setup(40, gpio.IN)  #echo

    time.sleep(0.030)
    gpio.output(38,True)
    time.sleep(0.00001) #10us
    gpio.output(38,False)
    while gpio.input(40) == 0:
        no_sig = time.time()
        
    while gpio.input(40) == 1:
        sig = time.time()
        
    tl = sig- no_sig #tl = time lenght
    
    if measure == 'cm':
        dis = tl / 0.000058 # lenght = (tl*34000)/2
    else:
        dis = None
        
        
    gpio.cleanup()
    return dis

print(distance('cm'))