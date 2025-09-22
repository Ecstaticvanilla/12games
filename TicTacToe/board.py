class Board:
    grid = []

    def __init__(self):
        for i in range(3):
            temp = [" " for i in range(3)]
            self.grid.append(temp)
        pass

    def printgrid(self):
        for i in range(3):
            print("-------------")
            print(f"| {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]} |")
        print("-------------")
        print()

    def setingrid(self,i,j,value):
        self.grid[i][j] = value

    def getvalue(self,i,j):
        return self.grid[i][j]

    def getemptyslots(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == " ":
                    moves.append([i,j]);
        return moves
    
    def isWin(self):
        lines = []

        lines.extend(self.grid)                    
        lines.extend(zip(*self.grid))              

        lines.append([self.grid[i][i] for i in range(3)])       
        lines.append([self.grid[i][2 - i] for i in range(3)])   

        for line in lines:
            if line[0] != " " and all(cell == line[0] for cell in line):
                return line[0], True

        return None, False