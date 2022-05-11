from gpiozero import Button, TrafficLights, Buzzer

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
                    lights.on()
                    buzzer.off()
                    button.wait_for_press()
                    lights.off()
                    buzzer.on()
                    button.wait_for_release()
                    


