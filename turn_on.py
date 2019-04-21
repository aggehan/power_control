import RPi.GPIO as GPIO
import time

# Settings
GPIO.setwarnings(False)

# Set pins
pin_5v_transitor = 17
#pin_3v3_transitor = 27

# Set what input names you are using
GPIO.setmode(GPIO.BCM)

# Both are outputs
GPIO.setup(pin_5v_transitor, GPIO.OUT)
#GPIO.setup(pin_3v3_transitor,GPIO.OUT)

# Let collector voltage go always (3v3)
# It will only trigger once the sensor sends out voltage
#GPIO.output(pin_3v3_transitor, True)

# Start the 5v_transitor to start the sensor
GPIO.output(pin_5v_transitor, True)

# Now the sensor should have 5v, and output a voltage based on the
# temperature, which in turn will start the 3.3 V, which will run through
# a resistor and then a led.

#Try it for 10 sec
time.sleep(1)
GPIO.output(pin_5v_transitor, False)
time.sleep(1)
GPIO.output(pin_5v_transitor, True)
time.sleep(1)
GPIO.output(pin_5v_transitor, False)
time.sleep(1)

# Clean up
GPIO.output(pin_5v_transitor, False) # Kill the power to the 5v
#GPIO.output(pin_3v3_transitor, False) # kill the power to the 3v3

# Clean up
GPIO.cleanup()
