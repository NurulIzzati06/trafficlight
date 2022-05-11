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
                button.wait_for_release()
                lights.amber.on(1)
                sleep (1)
                button.wait_for_release()
                lights.red.on(1)
                sleep (1)
             button.wait_for_release()
                buzzer.off()
                lights.off()
                buzzer.on()
                button.wait_for_release()



