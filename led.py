import neopixel

class LED:
    def __init__(self,led):
        self.led = led

    def ChangeColor(self,Color):
        self.led = Color
    def Clear(self):
        self.led = (0,0,0)
