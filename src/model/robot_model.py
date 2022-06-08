import RPi.GPIO as gpio
import time


in1 = 8
in2 = 10
en1 = 32
in3 = 16
in4 = 18
en2 = 33

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD) #BCM:GPIO/BOARD:pin number board
gpio.setup(in1,gpio.OUT)   
gpio.setup(in2,gpio.OUT)   
gpio.setup(en1,gpio.OUT)
gpio.setup(in3,gpio.OUT)   
gpio.setup(in4,gpio.OUT)   
gpio.setup(en2,gpio.OUT)
gpio.setup(36,gpio.OUT) #setup for servo motor

gpio.output(in1,gpio.LOW)   
gpio.output(in2,gpio.LOW)   
gpio.output(en1,gpio.LOW)
gpio.output(in3,gpio.LOW)   
gpio.output(in4,gpio.LOW)   
gpio.output(en2,gpio.LOW)

p1=gpio.PWM(en1,1000) #create PWM at channel en1 with 1000hz
p2=gpio.PWM(en2,1000)

speed = 50;


servo1 = gpio.PWM(36,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
#p1.start(100) #start PWM at cycle 50%
#p2.start(100)
servo1.start(0)

def stop():
    gpio.output(in1,gpio.LOW)   
    gpio.output(in2,gpio.LOW)   
    gpio.output(en1,gpio.LOW)
    gpio.output(in3,gpio.LOW)   
    gpio.output(in4,gpio.LOW)   
    gpio.output(en2,gpio.LOW)

def forward():
    #change_speed(speed)
    #change_speed()
    #p1.ChangeDutyCycle(5)
    #p2.ChangeDutyCycle(5)
    gpio.output(in1, gpio.LOW)   
    gpio.output(in2, gpio.HIGH) 

    gpio.output(in3, gpio.HIGH)   
    gpio.output(in4, gpio.LOW) 

    #gpio.output(en1,gpio.HIGH)
    #gpio.output(en2,gpio.HIGH)

    # gpio.cleanup()        #clean up all the port i have used
    print("forward")

    
def reverse():
    #change_speed(speed)
    #change_speed(speed)
    #p1.ChangeDutyCycle(100)
    #p2.ChangeDutyCycle(100)
    gpio.output(in1, gpio.HIGH)   
    gpio.output(in2, gpio.LOW) 

    gpio.output(in3, gpio.LOW)   
    gpio.output(in4, gpio.HIGH) 

    #gpio.output(en1,gpio.HIGH)
    #gpio.output(en2,gpio.HIGH)
    #gpio.cleanup()        #clean up all the port i have used
    print("reverse")
    
    
def turn_left():
    #change_speed(speed)
    #p1.ChangeDutyCycle(25)
    #p2.ChangeDutyCycle(25)
    gpio.output(in1, gpio.LOW)   
    gpio.output(in2, gpio.HIGH) 

    gpio.output(in3, gpio.LOW)   
    gpio.output(in4, gpio.HIGH) 

    #gpio.output(en1,gpio.HIGH)
    #gpio.output(en2,gpio.HIGH)
    #gpio.cleanup()        #clean up all the port i have used
    print("turn_left")

    
def turn_right():
    #change_speed(speed)
    #p1.ChangeDutyCycle(25)
    #p2.ChangeDutyCycle(25)
    gpio.output(in1, gpio.HIGH)   
    gpio.output(in2, gpio.LOW) 

    gpio.output(in3, gpio.HIGH)   
    gpio.output(in4, gpio.LOW) 

    #gpio.output(en1,gpio.HIGH)
    #gpio.output(en2,gpio.HIGH)
    #gpio.cleanup()        #clean up all the port i have used
    print("turn_right")

def change_speed(speed):
    print(speed)
    p1.start(speed) #start PWM at cycle 50%
    p2.start(speed)
    #p1.ChangeDutyCycle(speed)
    #p2.ChangeDutyCycle(speed)
    
def camera_turnleft():   
    servo1.ChangeDutyCycle(12)
    time.sleep(0.05)
    servo1.ChangeDutyCycle(0)
    
def camera_turnright():   
    servo1.ChangeDutyCycle(2)
    time.sleep(0.05)
    servo1.ChangeDutyCycle(0)
    
def camera_straight():
    servo1.ChangeDutyCycle(7)
    time.sleep(0.05)
    servo1.ChangeDutyCycle(0)
