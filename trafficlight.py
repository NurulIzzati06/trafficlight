from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    print(button.is_pressed)
    while True:
        if button.is_pressed:
            print("Hello")
        else:
            print("Goodbye")
            
            while True:
                button.wait_for_press()
                lights.green.on()
                sleep (1)
                lights.green.off()
                lights.amber.on()
                sleep (1)
                lights.amber.off()
                lights.red.on()
                sleep (1)
                lights.red.off()
                buzzer.off()
                lights.off()
                buzzer.on()
                



