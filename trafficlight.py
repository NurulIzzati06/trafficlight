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
                 lights.blink()
                 button.wait_for_press()
                 lights.off()
                 button.wait_for_release()


