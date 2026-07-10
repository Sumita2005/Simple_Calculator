import RPi.GPIO as GPIO
from time import sleep  

"""
class ledRBG():
    def__init__(self,R,B,G):
        Self.R = R
        self.B = B
        self.G = G
        GPIO.setup(self.R, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.G, GPIO.OUT)
    
    def color(self,mycolor):
        if mycolor == "red":
            GPIO.output(self.R, GPIO.LOW)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.HIGH)
        elif mycolor == "blue":
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.LOW)
            GPIO.output(self.G, GPIO.HIGH)
        elif mycolor == "green":
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.LOW)



#       R   B    G
pins = [17, 27, 22]  # GPIO pins to be used 
GPIO.setmode(GPIO.BCM)  # Set the GPIO mode to BCM
GPIO.setup(pins[0], GPIO.OUT)  # Set the GPIO pins as output
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)

while True:

    #RED
    GPIO.output(pins[0], GPIO.LOW)  # Turn off the red LED
    GPIO.output(pins[1], GPIO.HIGH)  
    GPIO.output(pins[2], GPIO.HIGH)  
    sleep(1)  

    #BLUE
    GPIO.output(pins[0], GPIO.HIGH)  # Turn on the red LED
    GPIO.output(pins[1], GPIO.LOW)  # Turn on the blue LED
    GPIO.output(pins[2], GPIO.HIGH)  # Turn on the green LED
    sleep(1) 
    
    #GREEN
    GPIO.output(pins[0], GPIO.HIGH)  # Turn on the red LED
    GPIO.output(pins[1], GPIO.HIGH)  # Turn on the blue LED
    GPIO.output(pins[2], GPIO.LOW)  # Turn on the green LED
    sleep(1)  """