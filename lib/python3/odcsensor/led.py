#!/usr/bin/env python3
"""
TODO: Module Docstring...
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class LED:
    """
    TODO: Function DocString...
    """
    def __init__(self, pin, freq=2000, is_inverse=False):
        """
        TODO: Function DocString...
        """ 
        self._pin = pin
        self._is_inverse = is_inverse
        GPIO.setup(self._pin, GPIO.OUT)
        GPIO.output(self._pin, GPIO.LOW)
        
        self._freq = freq
        self._duty_cycle = 0 if not self._is_inverse else 100
        self._pwm = GPIO.PWM(self._pin, self._freq)
        self._pwm.start(self._duty_cycle)
    def __del__(self):
        """
        TODO: Function DocString...
        """ 
        self._pwm.stop()
        GPIO.output(self._pin, GPIO.LOW)

    def set_freq(self, freq):
        """
        TODO: Function DocString...
        """ 
        self._freq = freq
        self._pwm.ChangeFrequency(freq)
    def set_duty_cycle(self, duty_cycle):
        """
        TODO: Function DocString...
        """ 
        dc = min(100,max(duty_cycle,0))
        self._duty_cycle = dc if not self._is_inverse else 100 - dc
        self._pwm.ChangeDutyCycle(self._duty_cycle)
    

    def set_on(self):
        """
        TODO: Function DocString...
        """
        self.set_duty_cycle(100)
        GPIO.output(self._pin, GPIO.HIGH)
    def set_off(self):
        """
        TODO: Function DocString...
        """
        self.set_duty_cycle(0)
        GPIO.output(self._pin, GPIO.LOW)


def class_test():
    """
    TODO: Function DocString...
    """
    #Basic Testing
    pins = (11,12)

    for pin in pins:
        LED1 = LED(pin)

        #Basic Turn on and off
        LED1.set_on()
        time.sleep(1)
        LED1.set_off()

        time.sleep(1)
        
        # Use simple PWM and off
        LED1.set_duty_cycle(50)
        time.sleep(1)
        LED1.set_off()

        time.sleep(2)

        # Turn slowly down
        for dc in range(100,-1,-1):
            LED1.set_duty_cycle(dc)
            time.sleep(0.1)
        del LED1

    GPIO.cleanup()


if __name__ == "__main__":
    class_test()