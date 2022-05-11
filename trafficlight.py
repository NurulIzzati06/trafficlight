from gpiozero import Button, LED

button = Button(21)
led = LED(25)

while True:
    print(button.is_pressed)
    while True:
        if button.is_pressed:
            print("Hello")
        else:
            print("Goodbye")
            while True:

                button.wait_for_press()
                led.on()
                button.wait_for_release()
                led.off()


