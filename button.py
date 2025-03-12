from machine import Pin

class Button:
    def __init__(self,pin,OnPress):
        self.pin = pin
        if(OnPress):
            self.button = Pin(self.pin, mode=Pin.IN, pull=Pin.PULL_DOWN)
            self.button.irq(trigger = Pin.IRQ_FALLING, handler = OnPress)
        else:
            self.button = Pin(self.pin,Pin.IN)
    def getvalue(self):
        return self.button.value()