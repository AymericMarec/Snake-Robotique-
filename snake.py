class Snake:
    def __init__(self,x,y):
        self.Body = [[x,y-2],[x,y-1],[x,y]]
        self.CurentDirection = "RIGHT"
        self.NextDirection = self.CurentDirection

    def DisplaySnake(self,Board):
        for i in range(0,len(self.Body)) :
            if(i == len(self.Body)-1):
                Board.Paint(self.Body[i][0],self.Body[i][1],(3,3,10))   #   On affiche la tete
            else :
                Board.Paint(self.Body[i][0],self.Body[i][1],(0,0,10))   #   On affiche le corps
        return Board
    
    def ChangeDirection(self,direction):
        self.NextDirection = direction
        
    def GetDirection(self):
        return self.CurentDirection

    def MoveSnake(self,Apple):
        NewHead = [self.Body[len(self.Body)-1][0],self.Body[len(self.Body)-1][1]] 
        if self.CurentDirection == "UP":
            NewHead[0]-=1
        elif self.CurentDirection == "RIGHT":
            NewHead[1]+=1
        elif self.CurentDirection == "DOWN":
            NewHead[0]+=1
        elif self.CurentDirection == "LEFT":
            NewHead[1]-=1
        #Si le joueur depasse les limites ou se rentre dedans , on renvoie une valeur autre que None qui met fin a la partie
        if(NewHead[0] < 0 or NewHead[0] >= 8 or NewHead[1] < 0 or NewHead[1] >= 8 or NewHead in self.Body):
            return "error"  
        if([Apple.x,Apple.y] != NewHead):   #   Si le joueur vient de manger une pomme , on lui retire pas de bout de queue
            self.Body.pop(0)
        self.Body.append(NewHead)
        return None