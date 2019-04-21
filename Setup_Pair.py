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

        GPIO.output(self.pin_on, True)
        GPIO.output(self.pin_off, True)

        GPIO.output(self.pin_on, False)
        GPIO.output(self.pin_off, False)


    def turn_on(self):
        print("its on")
        GPIO.output(self.pin_on, True)
        time.sleep(1)
        GPIO.output(self.pin_on, False)



    def turn_off(self):
        print("its off")
        GPIO.output(self.pin_off, True)
        time.sleep(1)
        GPIO.output(self.pin_off, False)

    def shutdown(self):
        GPIO.cleanup()
        quit()




A = PowerController(17,27)

A.init_pi_pins()
print("init pins done")
time.sleep(10)
A.turn_on()
time.sleep(10)
A.turn_off()
time.sleep(50)
print(" Shutdown NOW")
A.shutdown()




#print(A.pin_off)
