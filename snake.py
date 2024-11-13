class Snake:
    def __init__(self,x,y):
        self.Body = [[x,y-2],[x,y-1],[x,y]]
        self.CuurentDirection = "RIGHT"
        self.NextDirection = "RIGHT"
        self.ToClear = []

    def DisplaySnake(self,np,Board):
        for pixel in self.ToClear:
            np[Board[pixel[0]][pixel[1]]] = (0,0,0)
        for i in range(0,len(self.Body)) :
            if(i == len(self.Body)-1):
                np[Board[self.Body[i][0]][self.Body[i][1]]] = (3,3,10) 
            else :
                np[Board[self.Body[i][0]][self.Body[i][1]]] = (0,0,10) 
        return np
    def MoveSnake(self,Apple):
        NewHead = [self.Body[len(self.Body)-1][0],self.Body[len(self.Body)-1][1]] 
        self.CuurentDirection = self.NextDirection
        if self.CuurentDirection == "UP":
            NewHead[0]-=1
        elif self.CuurentDirection == "RIGHT":
            NewHead[1]+=1
        elif self.CuurentDirection == "DOWN":
            NewHead[0]+=1
        elif self.CuurentDirection == "LEFT":
            NewHead[1]-=1
        if(NewHead[0] < 0 or NewHead[0] >= 8 or NewHead[1] < 0 or NewHead[1] >= 8 or NewHead in self.Body):
            return "error"
        if(Apple != NewHead):
            self.Body.pop(0)
        self.Body.append(NewHead)
        return None
