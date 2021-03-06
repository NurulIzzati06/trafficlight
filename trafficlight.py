from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    print(button.is_pressed)
    
    button.wait_for_press()
        
    if button.is_pressed:
        print("Button pressed.")
        
        # green on
        lights.green.on()
        sleep (1.5)
        
        # green off
        lights.green.off()
        sleep(1)
        
        # amber on
        lights.amber.on()
        sleep(0.5)
        lights.amber.off()
        sleep(0.5)
        lights.amber.on()
        sleep(0.5)
        lights.amber.off()
        sleep(1)
        
        # red, buzzer on
        lights.red.on()
        buzzer.on()
        sleep (2)
        
        # all light & buzzer off
        lights.red.off()
        lights.off()
        buzzer.off()
        sleep(1.5)

        # green on
        lights.green.on()
        sleep (1.5)
        
        # green off
        lights.green.off()
        sleep(1)

        # amber on
        lights.amber.on()
        sleep(0.5)
        lights.amber.off()
        sleep(0.5)
        lights.amber.on()
        sleep(0.5)
        lights.amber.off()
        sleep(1)

        # red, buzzer on
        lights.red.on()
        buzzer.on()
        sleep (2)
        
        # all light & buzzer off
        lights.red.off()
        lights.off()
        buzzer.off()
        sleep(1.5)
    
    else:
        print("Goodbye")
        
                
                
                



