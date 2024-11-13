import neopixel
import machine
import led

class Grid:
    def __init__(self):
        self.LED_PIN = 1
        self.NB_LED = 64
        self.np = neopixel.NeoPixel(machine.Pin(self.LED_PIN), self.NB_LED)
        self.LEDGrid = self.InitTab()

    def InitTab(self):
        leds = []
        for column in range(0,8):
            TheRow = []
            for row in range(0,8):
                print(column,row)
                print(self.np[0])
                Led = led.LED(self.np[column*row])
                TheRow.append(Led)
            leds.append(TheRow)

        # leds = []
        # for i in range (0,nbLed):
        #     leds.append(i)
        BetterLED = []
        for i in range(0,8):
            row = leds[i*8:(i+1)*8]
            if(i%2 != 0):
                row.reverse()
            BetterLED.append(row)
        return BetterLED