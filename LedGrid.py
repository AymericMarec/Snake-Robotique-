from neopixel import NeoPixel
from machine import Pin
from time import sleep

class LedGrid:
    def __init__(self,LED_PIN,NB_LED):
        self.LED_PIN = LED_PIN
        self.NB_LED = NB_LED
        self.np = NeoPixel(Pin(self.LED_PIN), self.NB_LED)
        self.LEDGrid = self.InitTab()

    #On créer un tableau qui comporte les nombres de 0 a 63 pour notre matrice de led
    #Puis on la transforme ce tableau en matrice de 8x8 et inversant une ligne sur 2
    #Pour avoir accès a une led precise grace a des coordonnées 
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
    #Eteindre toute les leds de la matrice  
    def clear_all(self) :
        for led in range(0,self.NB_LED):
            self.np[led] =(0,0,0)
        self.np.write()
    #Allumer une led precisemment avec une couleur
    def Paint(self,x,y,Color):
        self.np[self.LEDGrid[x][y]] = Color
     
    def Refresh(self):
        self.np.write()
    #Renvoie une matrice representant la matrice de led avec des "1" pour representer des leds a allumer
    def TabNB(self,nb):
        if(nb == 3):
            return[
            ["0","0","0","0","0","0","0","0"],
            ["0","0","1","1","1","1","0","0"],
            ["0","0","0","0","0","0","1","0"],
            ["0","0","0","0","0","0","1","0"],
            ["0","0","1","1","1","1","0","0"],
            ["0","0","0","0","0","0","1","0"],
            ["0","0","0","0","0","0","1","0"],
            ["0","0","1","1","1","1","0","0"]
            ] 
        elif(nb == 2):
            return[
            ["0","0","1","1","1","1","0","0"],
            ["0","1","0","0","0","0","1","0"],
            ["0","1","0","0","0","0","1","0"],
            ["0","0","0","0","0","0","1","0"],
            ["0","0","0","0","1","1","0","0"],
            ["0","0","1","1","0","0","0","0"],
            ["0","1","0","0","0","0","0","0"],
            ["0","1","1","1","1","1","1","0"]
            ] 
        elif(nb == 1):
            return[
            ["0","0","0","0","0","0","0","0"],
            ["0","0","0","1","1","0","0","0"],
            ["0","0","0","1","1","0","0","0"],
            ["0","0","0","1","1","0","0","0"],
            ["0","0","0","1","1","0","0","0"],
            ["0","0","0","1","1","0","0","0"],
            ["0","0","0","1","1","0","0","0"],
            ["0","0","0","0","0","0","0","0"]
            ] 
    #On Dessine la matrice qu'on a recu
    def DrawTab(self,tabNB,Color):
        for row in range(0,len(tabNB)):
            tabNB[row].reverse()
            for led in range(0,len(tabNB[row])):
                if(tabNB[row][led] == "1"):
                    self.Paint(row,led,Color)
        self.Refresh()
    #On affiche un compteur avant de démarrer la partie
    def CountDown(self):
        Color = (10,0,0)
        for CountDown in range(3,0,-1): #   Une boucle ou CountDown prends les valeurs 3,2,1
            TabNB = self.TabNB(CountDown)
            self.DrawTab(TabNB,Color)
            sleep(1)
            self.clear_all()

