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

        GPIO.output(self.pin_on, False)
        GPIO.output(self.pin_off, False)


    def turn_on(self):
        print("its on")

    def shutdown(self):
        GPIO.cleanup()
        quit()




pc_A = PowerController(17,27)

pc_A.turn_on()



#print(A.pin_off)
