from machine import Pin

class Button:
    def __init__(self,pin,OnPress):
        self.pin = pin
        self.button = self.Init(OnPress)
        
    def Init(self,OnPress):
        # creation du bouton avec le pin souhaité , en mode lecture , en forcant le bouton a etre utilisé en tant que trigger
        button = Pin(self.pin, mode=Pin.IN, pull=Pin.PULL_DOWN)
        # irq permet de faire une interuption ,et de declancher une fonction , si l'evenement
        # Pin.IRQ_FALLING arrive , soit , l'appui du bouton
        button.irq(trigger = Pin.IRQ_FALLING, handler = OnPress)