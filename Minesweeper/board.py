import random 

class Cell:
    flagged = False
    visible = False
    value = 0
    def __init__(self,value,visible,flagged):
        self.value = value
        self.visible = visible 
        self.flagged = flagged

    def setFlag(self):
        self.flagged = not (self.flagged)
    
    def setVisible(self):
        self.visible = True

    
class Board:
    size = 10
    board = []
    mines = 0

    def __init__(self, size):
        self.size = size
        self.board = [[Cell(0,False,False) for _ in range(size)] for _ in range(size)]
        self.mines = random.randint(int(size**2*0.1), int(size**2*0.15))
    
    def createboard(self):
        temp = self.mines
        probablity = self.mines/(self.size**2)
        while temp > 0:
            for i in range(self.size):
                for j in range(self.size):
                    if random.random() <= probablity:
                        self.board[i][j].value = -1
                        temp -= 1
        directions = [(-1,-1), (-1,0), (-1,1),
                    (0,-1),          (0,1),
                    (1,-1),  (1,0),  (1,1)]

        for i in range(self.size):
            for j in range(self.size):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < self.size and 0 <= nj < self.size and self.board[i][j].value != -1:
                        if self.board[ni][nj].value == -1:
                            self.board[i][j].value += 1
        return self.mines
    
    def printboard(self, debug=False):
        def cell_repr(cell):
            if debug:
                return str(cell.value)
            if cell.visible:
                return str(cell.value)
            if cell.flagged:
                return "F"
            return " "
        
        for i in range(self.size):
            print("-----" * (self.size) + "-")
            for j in range(self.size):
                print(f"| {cell_repr(self.board[i][j]):^2}", end=" ")
            print("|")
        print("-----" * (self.size) + "-")


    def dig(self,i,j):
        if self.board[i][j].visible:
            return False
        if self.board[i][j].value== -1:
            return True
        if self.board[i][j].flagged:
            x = input("Flagged!!! Can you confirm if you want to dig?(y/n) : ")
            if x == 'y':
                self.board[i][j].setVisible()
        else:
            self.board[i][j].setVisible()
        directions = [(-1,-1), (-1,0), (-1,1),
                    (0,-1),          (0,1),
                    (1,-1),  (1,0),  (1,1)]
        neighbors = []
        if self.board[i][j].value == 0:
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < self.size and 0 <= nj < self.size:
                    if self.board[ni][nj].value != -1 and not self.board[ni][nj].visible :
                        self.dig(ni,nj)                
        return False



    def flag(self,i,j):
        if self.board[i][j].visible:
            return 0
        changeinflagvalue = -1
        if  self.board[i][j].flagged:
            changeinflagvalue = 1
        self.board[i][j].setFlag() 
        return changeinflagvalue

    def isWin(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].value != 1:
                    if not self.board[i][j].visible:
                        return False
        return True
