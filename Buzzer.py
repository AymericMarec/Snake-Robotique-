from machine import PWM,Pin
from time import sleep

class Buzzer :
    def __init__(self,pin) :
        self.buzzer = PWM(Pin(pin))
        
    def Play(self,frequency,duration):
        self.buzzer.freq(frequency)
        self.buzzer.duty(50)
        sleep(duration)
        self.buzzer.duty(0)

    def Stop(self):
        self.buzzer.value(0)

    def DrowningLove(self):
        self.Play(277,0.15)
        self.Play(349,0.15)
        self.Play(466,0.15)
        self.Play(523,0.15)
        self.Play(554,0.15)
        self.Play(739,0.15)

        self.Play(415,0.15)
        self.Play(440,0.15)
        self.Play(523,0.15)
        self.Play(554,0.15)
        self.Play(523,0.15)
        self.Play(440,0.15)

        self.Play(369,0.15)
        self.Play(440,0.15)
        self.Play(523,0.15)
        self.Play(554,0.15)
        self.Play(523,0.15)
        self.Play(440,0.15)

        self.Play(349,0.15)
        self.Play(440,0.15)
        self.Play(523,0.15)
        self.Play(554,0.15)
        self.Play(622,0.15)
if __name__ == "__main__":
    buzzer = Buzzer(7)
    # buzzer.Play(277,0.15)
    # buzzer.Play(450,0.15)
    # buzzer.Play(739,0.15)
    while True:
        buzzer.DrowningLove()
