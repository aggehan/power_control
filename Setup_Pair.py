# Since each power controller have an on and off controller,
# the pair of the two must be set properly and their position
# on the raspberry must be good.
import RPi.GPIO as GPIO
import time


class PowerController:
    def __init__(self, pin_on, pin_off):
        self.pin_on = pin_on
        self.pin_off = pin_off

    def init_pi_pins(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin_on, GPIO.OUT)
        GPIO.setup(self.pin_off, GPIO.OUT)

        #GPIO.output(self.pin_on, True)
        #GPIO.output(self.pin_off, True)

        GPIO.output(self.pin_on, False)
        GPIO.output(self.pin_off, False)


    def turn_on(self):
        print("On Start")

        # Spam press the button
        counter = 1
        while counter<=6:
            # Make sure it is off
            GPIO.output(self.pin_off, False)
            # Turn on
            GPIO.output(self.pin_on, True)
            time.sleep(1)
            GPIO.output(self.pin_on, False)
            #increment
            counter = counter + 1
        print("On End.")


    def turn_off(self):
        print("Off Start")

        # Spam press the button
        counter = 1
        while counter<=6:
            # Make sure it is off
            GPIO.output(self.pin_on, False)
            # Turn on
            GPIO.output(self.pin_off, True)
            time.sleep(1)
            GPIO.output(self.pin_off, False)
            #increment
            counter = counter + 1

        print("Off End.")


    def shutdown(self):
        print(" Shutdown NOW")
        GPIO.output(self.pin_on, False)
        GPIO.output(self.pin_off, False)
        GPIO.cleanup()
        quit()




A = PowerController(17,27)

A.init_pi_pins()
A.turn_on()
A.turn_off()
A.shutdown()
