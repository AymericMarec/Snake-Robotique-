from random import randint

class Apple:
    def __init__(self,Snake):
        self.x = 0
        self.y = 0
        self.SpawnApple(Snake)

    def SpawnApple(self,Snake):
        self.x = randint(0,7)
        self.y = randint(0,7)
        while [self.x,self.y] in Snake.Body:
            self.x = randint(0,7)
            self.y = randint(0,7)
