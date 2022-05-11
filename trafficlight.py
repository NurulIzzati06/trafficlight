from gpiozero import Button

button = Button(21)

while True:
    print(button.is_pressed)
    while True:
        if button.is_pressed:
            print("Hello")
        else:
            print("Goodbye")
            while True:

                button.wait_for_press()
                print("Pressed")
                button.wait_for_release()
                print("Released")


