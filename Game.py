from snake import Snake
from LedGrid import LedGrid
from button import Button
from random import randint
from apple import Apple
from time import sleep
from joystick import Joystick
from buzzer import Buzzer


class Game:
    def __init__(self):
        self.snake = Snake(3,3)
        self.apple = Apple(self.snake)
        self.LedGrid = LedGrid(1,64)
        self.Points = 0
        self.Joystick = Joystick(4,5)
        self.Button = Button(6,None)
        self.Menu()

    def Menu(self):
        print("-------------------------------\n")
        print("Choisir une difficulté : \n")
        print("Haut - Facile")
        print("Droite - Moyen")
        print("Bas - Difficile")
        print("Gauche - Impossible")
        print("\n-------------------------------")
        speed = 0
        while True:
            direction = self.Joystick.GetDirection(self.snake)
            if(direction == "UP"):
                speed = 1
                break
            elif(direction == "RIGHT"):
                speed = 0.5
                break
            elif(direction == "DOWN"):
                speed = 0.2
                break
            elif(direction == "LEFT"):
                speed = 0.1
                break
            sleep(0.1)
        self.StartGame(speed)


    def StartGame(self,speed):
        self.LedGrid.CountDown()
        while True:
            direction = self.Joystick.GetDirection(self.snake)
            print(direction)
            if(direction):
                if(direction == "UP" and self.snake.CurentDirection != "DOWN"):
                    self.snake.CurentDirection = direction
                elif(direction == "RIGHT" and self.snake.CurentDirection != "LEFT"):
                    self.snake.CurentDirection = direction
                elif(direction == "DOWN" and self.snake.CurentDirection != "UP"):
                    self.snake.CurentDirection = direction
                elif(direction == "LEFT" and self.snake.CurentDirection != "RIGHT"):
                    self.snake.CurentDirection = direction
            err = self.snake.MoveSnake(self.apple)
            if err != None :    #   Si le joueur perd
                print(f"Tu as perdu avec : {self.Points} points")
                return
            self.LedGrid = self.snake.DisplaySnake(self.LedGrid)
            if [self.apple.x,self.apple.y] in self.snake.Body:  #   Si le joueur mange une pomme
                self.Points+=1
                print(f"Points : {self.Points}")
                self.apple.SpawnApple(self.snake)

            self.LedGrid.Paint(self.apple.x,self.apple.y,(0,10,0))  #   On affiche la pomme
            self.LedGrid.Refresh()
            sleep(speed)
            self.LedGrid.clear_all()
