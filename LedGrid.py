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
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
            ] 
        elif(nb == 2):
            return[
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
            ] 
        elif(nb == 1):
            return[
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
            ]

    def CountDown(self):
        # oui je fais nettoyer cette fonction t'inquetes
        Color = (10,0,0)
        self.clear_all()
        TabNB = self.TabNB(3)
        for row in range(0,len(TabNB)):
            for led in range(0,len(TabNB[row])):
                if(led == "1"):
                    self.Paint(row,led,(10,0,0))
        self.Refresh()


                    
        # np[Board[0][3]] = Color
        # np[Board[0][4]] = Color
        # np[Board[0][5]] = Color
        # np[Board[1][2]] = Color
        # np[Board[2][2]] = Color
        # np[Board[3][3]] = Color
        # np[Board[3][4]] = Color
        # np[Board[3][5]] = Color
        # np[Board[4][2]] = Color
        # np[Board[5][2]] = Color
        # np[Board[6][3]] = Color
        # np[Board[6][4]] = Color
        # np[Board[6][5]] = Color
        time.sleep(1)
        self.clear_all()
        TabNB = self.TabNB(2)
        for row in range(0,len(TabNB)):
            for led in range(0,len(TabNB[row])):
                if(led == "1"):
                    self.Paint(row,led,(10,0,0))
        # np[Board[0][2]] = Color
        # np[Board[0][3]] = Color
        # np[Board[0][4]] = Color
        # np[Board[0][5]] = Color
        # np[Board[1][2]] = Color
        # np[Board[2][2]] = Color
        # np[Board[2][3]] = Color
        # np[Board[3][4]] = Color
        # np[Board[3][5]] = Color
        # np[Board[4][6]] = Color
        # np[Board[5][6]] = Color
        # np[Board[6][2]] = Color
        # np[Board[6][3]] = Color
        # np[Board[6][4]] = Color
        # np[Board[6][5]] = Color
        # np[Board[0][6]] = Color
        time.sleep(1)
        self.clear_all()
        TabNB = self.TabNB(1)
        for row in range(0,len(TabNB)):
            for led in range(0,len(TabNB[row])):
                if(led == "1"):
                    self.Paint(row,led,(10,0,0))
        # np[Board[1][3]] = Color
        # np[Board[2][3]] = Color
        # np[Board[3][3]] = Color
        # np[Board[4][3]] = Color
        # np[Board[5][3]] = Color
        # np[Board[6][3]] = Color
        # np[Board[1][4]] = Color
        # np[Board[2][4]] = Color
        # np[Board[3][4]] = Color
        # np[Board[4][4]] = Color
        # np[Board[5][4]] = Color
        # np[Board[6][4]] = Color
        time.sleep(1)

        self.clear_all()

