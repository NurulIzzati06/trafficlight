from gpiozero import Button, TrafficLights

button = Button(21)
lights = TrafficLights(25, 8, 7)

while True:
    print(button.is_pressed)
    while True:
        if button.is_pressed:
            print("Hello")
        else:
            print("Goodbye")
            
            while True:
                 button.wait_for_press()
                 lights.on()
                 button.wait_for_release()
                 lights.off()


