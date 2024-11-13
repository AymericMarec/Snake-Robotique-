import neopixel
import time
import machine
from random import randint
import snake

def CountDown(np,Board):
    # oui je fais nettoyer cette fonction t'inquetes
    Color = (10,0,0)
    clear_all()
    np[Board[0][3]] = Color
    np[Board[0][4]] = Color
    np[Board[0][5]] = Color
    np[Board[1][2]] = Color
    np[Board[2][2]] = Color
    np[Board[3][3]] = Color
    np[Board[3][4]] = Color
    np[Board[3][5]] = Color
    np[Board[4][2]] = Color
    np[Board[5][2]] = Color
    np[Board[6][3]] = Color
    np[Board[6][4]] = Color
    np[Board[6][5]] = Color
    np.write()
    time.sleep(1)
    clear_all()
    np[Board[0][2]] = Color
    np[Board[0][3]] = Color
    np[Board[0][4]] = Color
    np[Board[0][5]] = Color
    np[Board[1][2]] = Color
    np[Board[2][2]] = Color
    np[Board[2][3]] = Color
    np[Board[3][4]] = Color
    np[Board[3][5]] = Color
    np[Board[4][6]] = Color
    np[Board[5][6]] = Color
    np[Board[6][2]] = Color
    np[Board[6][3]] = Color
    np[Board[6][4]] = Color
    np[Board[6][5]] = Color
    np[Board[0][6]] = Color
    np.write()
    time.sleep(1)
    clear_all()

    np[Board[1][3]] = Color
    np[Board[2][3]] = Color
    np[Board[3][3]] = Color
    np[Board[4][3]] = Color
    np[Board[5][3]] = Color
    np[Board[6][3]] = Color
    np[Board[1][4]] = Color
    np[Board[2][4]] = Color
    np[Board[3][4]] = Color
    np[Board[4][4]] = Color
    np[Board[5][4]] = Color
    np[Board[6][4]] = Color
    np.write()
    time.sleep(1)

    clear_all()


def InitTab(nbLed):
    leds = []
    for i in range (0,nbLed):
        leds.append(i)
    BetterLED = []
    for i in range(0,8):
        row = leds[i*8:(i+1)*8]
        if(i%2 != 0):
            row.reverse()
        BetterLED.append(row)
    return BetterLED
        
def clear_all() :
    for i in range(0,NB_LED):
        np[i] =(0,0,0)
    np.write()

def SpawnApple(Snake):
    AppleX = randint(0,7)
    AppleY = randint(0,7)
    while [AppleX,AppleY] in Snake.Body:
        AppleX = randint(0,7)
        AppleY = randint(0,7)
    return [AppleX,AppleY]

def ChangeDirection(pin):
    global TheSnake
    global OnMenu
    global Timer
    if pin == buttonup and TheSnake.CuurentDirection!= "DOWN":
        TheSnake.NextDirection = "UP"
    elif pin == buttonright and TheSnake.CuurentDirection!= "LEFT":
        TheSnake.NextDirection = "RIGHT"
    elif pin == buttondown and TheSnake.CuurentDirection!= "UP":
        TheSnake.NextDirection = "DOWN"
    elif pin == buttonleft and TheSnake.CuurentDirection!= "RIGHT":
        TheSnake.NextDirection = "LEFT"

def Paint(np,Board,x,y,Color):
    np[Board[x][y]] = Color
    return np

def Menu():
    print("------------------------\n\n")
    print("     Touches :\n")
    print(" - Bouton 1 : Haut\n")
    print(" - Bouton 2 : Bas\n")
    print(" - Bouton 3 : Gauche\n")
    print(" - Bouton 4 : Droite\n")


def Game(np,Board):
    Points = 0
    global TheSnake
    TheSnake = snake.Snake(3,3)
    Apple = SpawnApple(TheSnake)
    while True:
        err = TheSnake.MoveSnake(Apple)
        if err != None :
            print(f"Tu as perdu avec : {Points} points")
            return
        np = TheSnake.DisplaySnake(np,Board)
        if Apple in TheSnake.Body:
            Points+=1
            print(f"Points : {Points}")
            Apple = SpawnApple(TheSnake)

        np[Board[Apple[0]][Apple[1]]] = (0,10,0)
        np.write()
        time.sleep(0.5)
        clear_all() 

LED_PIN = 1
BUTTON_UP_PIN = 20
BUTTON_RIGHT_PIN = 19
BUTTON_DOWN_PIN = 21
BUTTON_LEFT_PIN = 18
NB_LED = 64

np = neopixel.NeoPixel(machine.Pin(LED_PIN), NB_LED)
buttonup = machine.Pin(BUTTON_UP_PIN, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
buttondown = machine.Pin(BUTTON_DOWN_PIN, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
buttonleft = machine.Pin(BUTTON_LEFT_PIN , mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
buttonright = machine.Pin(BUTTON_RIGHT_PIN, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)

buttonup.irq(trigger = machine.Pin.IRQ_FALLING, handler = ChangeDirection)
buttondown.irq(trigger = machine.Pin.IRQ_FALLING, handler = ChangeDirection)
buttonleft.irq(trigger = machine.Pin.IRQ_FALLING, handler = ChangeDirection)
buttonright.irq(trigger = machine.Pin.IRQ_FALLING, handler = ChangeDirection)

Board = InitTab(NB_LED)
Menu()
CountDown(np,Board)
Game(np,Board)