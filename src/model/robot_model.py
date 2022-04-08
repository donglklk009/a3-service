# import RPi.GPIO as gpio
import time

def init():
    # gpio.setmode(gpio.BOARD) #BCM:GPIO/BOARD:pin number board
    # gpio.setup(7,gpio.OUT)   
    # gpio.setup(11,gpio.OUT)   
    # gpio.setup(13,gpio.OUT)
    # gpio.setup(15,gpio.OUT)

    # gpio.setup(12,gpio.OUT)   
    # gpio.setup(16,gpio.OUT)   
    # gpio.setup(18,gpio.OUT)
    # gpio.setup(22,gpio.OUT)
    pass


def forward(ts):          #ts:time sleep
    # gpio.output(7,True)   
    # gpio.output(11,False) 
    # gpio.output(13,False)  
    # gpio.output(15,True) 
    # gpio.output(12,True)   
    # gpio.output(16,False) 
    # gpio.output(18,False)  
    # gpio.output(22,True) 
    time.sleep(ts)        #time sleep in second
    # gpio.cleanup()        #clean up all the port i have used
    print("forward")
    pass

    
def reverse(ts):        
    # gpio.output(7,False)   
    # gpio.output(11,True)  
    # gpio.output(13,True)  
    # gpio.output(15,False) 
    # gpio.output(12,False)   
    # gpio.output(16,True) 
    # gpio.output(18,True)  
    # gpio.output(22,False) 
    time.sleep(ts)        
    # gpio.cleanup()      
    print("reverse")
    pass
    
    
def turn_left(ts):       
    # gpio.output(7,False)   
    # gpio.output(11,True)  
    # gpio.output(13,True)  
    # gpio.output(15,False) 
    # gpio.output(12,True)   
    # gpio.output(16,False) 
    # gpio.output(18,False)  
    # gpio.output(22,True) 
    time.sleep(ts)        
    # gpio.cleanup()
    print("turn_left")
    pass

    
def turn_right(ts):       
    # gpio.output(7,True)   
    # gpio.output(11,False)  
    # gpio.output(13,False)  
    # gpio.output(15,True) 
    # gpio.output(12,False)   
    # gpio.output(16,True) 
    # gpio.output(18,True)  
    # gpio.output(22,False) 
    time.sleep(ts)        
    # gpio.cleanup()
    print("turn_right")
    pass

    