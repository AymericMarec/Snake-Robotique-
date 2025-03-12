from machine import ADC,Pin
from time import sleep

class Joystick:
    def __init__(self,pinX,pinY):
        # ADC = Analog-to-Digital Converter
        #initalisation des joystick en donnant la posibilité de lire l'axe X et Y du joystick
        self.xVal=ADC(Pin(pinX, Pin.IN))
        self.yVal=ADC(Pin(pinY, Pin.IN))
        # attenue le signal d'entrée de 11db pour une plage de tension de 0V - 3.6V au lieu de 0 - 1.1V
        self.xVal.atten(ADC.ATTN_11DB)
        self.yVal.atten(ADC.ATTN_11DB)
        # les valeurs du joystick en X et Y seront en 12 bit soit entre 0 et 4095 

    def GetDirection(self,snake):
        coX = self.xVal.read()
        coY = self.yVal.read()
        if(coY < 500):
            return "UP"
        elif coY > 4000 :
            return "DOWN"
        elif coX < 500 :
            return "RIGHT"
        elif coX > 4000 :
            return "LEFT"
        return ""
    
if __name__ == "__main__":
    joystick = Joystick(4,5)
    while True:
        coX = joystick.xVal.read()
        coY = joystick.yVal.read()
        print(coX,coY)	
        sleep(0.5)
        

