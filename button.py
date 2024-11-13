import machine

class Button:
    def __init__(self,pin,OnPress):
        self.pin = pin
        self.button = self.Init(OnPress)
        
    def Init(self,OnPress):
        button = machine.Pin(self.pin, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
        button.irq(trigger = machine.Pin.IRQ_FALLING, handler = OnPress)