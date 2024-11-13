import neopixel
import machine
import time

class LedGrid:
    def __init__(self,LED_PIN,NB_LED):
        self.LED_PIN = LED_PIN
        self.NB_LED = NB_LED
        self.np = neopixel.NeoPixel(machine.Pin(self.LED_PIN), self.NB_LED)
        self.LEDGrid = self.InitTab()

    def InitTab(self):
        leds = []
        for i in range (0,self.NB_LED):
            leds.append(i)
        BetterLED = []
        for i in range(0,8):
            row = leds[i*8:(i+1)*8]
            if(i%2 != 0):
                row.reverse()
            BetterLED.append(row)
        return BetterLED
            
    def clear_all(self) :
        for i in range(0,self.NB_LED):
            self.np[i] =(0,0,0)
        self.np.write()

    def Paint(self,x,y,Color):
        self.np[self.LEDGrid[x][y]] = Color
        
    def Refresh(self):
        self.np.write()
    def TabNB(self,nb):
        if(nb == 3):
            return[
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"]
            ] 
        elif(nb == 2):
            return[
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"]
            ] 
        elif(nb == 1):
            return[
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0"]
            ] 
    def DrawNB(self,tab,Color):
        self.clear_all()
        for row in range(0,len(tab)):
            for led in range(0,len(tab[row])):
                if(led == "1"):
                    self.Paint(row,led,Color)
        self.Refresh()
    def CountDown(self):
        Color = (10,0,0)
        TabNB = self.TabNB(3)
        self.DrawNB(TabNB,Color)
        time.sleep(1)
        TabNB = self.TabNB(2)
        self.DrawNB(TabNB,Color)
        time.sleep(1)
        TabNB = self.TabNB()
        self.DrawNB(TabNB,Color)
        time.sleep(1)

