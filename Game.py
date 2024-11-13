from snake import Snake
from LedGrid import LedGrid
from button import Button
from random import randint
from Apple import Apple
from time import sleep

class Game:
    def __init__(self):
        self.snake = Snake(3,3)
        self.apple = Apple(self.snake)
        self.LedGrid = LedGrid(1,64)
        self.Points = 0
        self.buttonUP = Button(20,self.ChangeDirection)
        self.buttonRIGHT = Button(19,self.ChangeDirection)
        self.buttonDOWN = Button(21,self.ChangeDirection)
        self.buttonLEFT = Button(18,self.ChangeDirection)
        self.Menu()
        self.StartGame()

    def ChangeDirection(self,pin):
        if pin == self.buttonUP and self.snake.CuurentDirection!= "DOWN":
            self.snake.NextDirection = "UP"
        elif pin == self.buttonRIGHT and self.snake.CuurentDirection!= "LEFT":
            self.snake.NextDirection = "RIGHT"
        elif pin == self.buttonDOWN and self.snake.CuurentDirection!= "UP":
            self.snake.NextDirection = "DOWN"
        elif pin == self.buttonLEFT and self.snake.CuurentDirection!= "RIGHT":
            self.snake.NextDirection = "LEFT"
    def SpawnApple(self):
        AppleX = randint(0,7)
        AppleY = randint(0,7)
        while [AppleX,AppleY] in self.Snake.Body:
            AppleX = randint(0,7)
            AppleY = randint(0,7)
        return [AppleX,AppleY]
    def Menu(self):
        print("------------------------\n\n")
        print("     Touches :\n")
        print(" - Bouton 1 : Haut\n")
        print(" - Bouton 2 : Bas\n")
        print(" - Bouton 3 : Gauche\n")
        print(" - Bouton 4 : Droite\n")

    def StartGame(self):
        while True:
            err = self.snake.MoveSnake(self.apple)
            if err != None :
                print(f"Tu as perdu avec : {self.Points} points")
                return
            self.LedGrid = self.snake.DisplaySnake(self.LedGrid)
            if Apple in self.snake.Body:
                Points+=1
                print(f"Points : {Points}")
                self.apple.SpawnApple(self.snake)

            self.LedGrid.Paint(self.apple.x,self.apple.y,(0,10,0))
            self.LedGrid.Refresh()
            sleep(0.5)
            self.LedGrid.clear_all()
