import RPi.GPIO as GPIO

inputButton=10
led=13
counter=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(inputButton, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    value = GPIO.input(inputButton)
    GPIO.output(led, False)
    if value == False:
        print("You pressed button:",counter)
        counter+=1
        #show led 13
        GPIO.output(led, True)
        while value == False:
            value = GPIO.input(inputButton)
            
