import neopixel
import machine

def ChangeDirection(pin):
    global TheSnake
    global OnMenu
    global Timer
    print(OnMenu)
    # if(OnMenu):
    #     if pin == buttonup:
    #         Timer = 1
    #     elif pin == buttondown:
    #         Timer = 0.5
    #     elif pin == buttonleft:
    #         Timer = 0.3
    #     OnMenu = False

    # else :
    if pin == buttonup and TheSnake.CuurentDirection!= "DOWN":
        TheSnake.NextDirection = "UP"
    elif pin == buttonright and TheSnake.CuurentDirection!= "LEFT":
        TheSnake.NextDirection = "RIGHT"
    elif pin == buttondown and TheSnake.CuurentDirection!= "UP":
        TheSnake.NextDirection = "DOWN"
    elif pin == buttonleft and TheSnake.CuurentDirection!= "RIGHT":
        TheSnake.NextDirection = "LEFT"

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
