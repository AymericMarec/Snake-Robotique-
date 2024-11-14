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
        self.StartGame()

    def ChangeDirection(self,pin):
        if pin == self.buttonUP.button and self.snake.GetDirection()!= "DOWN":
            self.snake.ChangeDirection("UP")
        elif pin == self.buttonRIGHT.button and self.snake.GetDirection()!= "LEFT":
            self.snake.ChangeDirection("RIGHT")
        elif pin == self.buttonDOWN.button and self.snake.GetDirection()!= "UP":
            self.snake.ChangeDirection("DOWN")
        elif pin == self.buttonLEFT.button and self.snake.GetDirection()!= "RIGHT":
            self.snake.ChangeDirection("LEFT")

    def StartGame(self):
        while True:
            err = self.snake.MoveSnake(self.apple)
            if err != None :    #   Si le joueur perd
                print(f"Tu as perdu avec : {self.Points} points")
                return
            self.LedGrid = self.snake.DisplaySnake(self.LedGrid)
            if [self.apple.x,self.apple.y] in self.snake.Body:  #   Si le joueur mange une pomme
                Points+=1
                print(f"Points : {Points}")
                self.apple.SpawnApple(self.snake)

            self.LedGrid.Paint(self.apple.x,self.apple.y,(0,10,0))  #   On affiche la pomme
            self.LedGrid.Refresh()
            sleep(0.5)
            self.LedGrid.clear_all()
