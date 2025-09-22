from random import randint,choice
import math

class Player:
    letter = " "
    def __init__(self,letter):
        self.letter = letter
        pass

    def move(self,board):
        #level redundant to match computer level 1
        while True:
            i,j = map(int, input("Enter where to add({i j}  format) --> ").split())
            if (i < 3 or j < 3 or i > 0 or j > 0) and board.getvalue(i,j) == " ":
                board.setingrid(i,j,self.letter)
                return
            print("Enter Valid !!")

class Computer(Player):
    def __init__(self,letter):
        super().__init__(letter)
        pass
    
    def move(self,board):
        while True:
            i,j = randint(0,2),randint(0,2)
            if board.getvalue(i,j) == " ":
                board.setingrid(i,j,self.letter)
                break
        
class GoodComputer(Player):
    def __init__(self,letter):
        super().__init__(letter)
        pass

    def minimax(self, state, letter):
        maxplayer = self.letter
        otherplayer = 'O' if letter == 'X' else 'X'

        winningletter, iswin = state.isWin()
        currempty = state.getemptyslots()

        if winningletter == maxplayer:
            return {"pos": None, "score": 1 * (len(currempty) + 1)}
        elif winningletter == otherplayer:
            return {"pos": None, "score": -1 * (len(currempty) + 1)}
        elif len(currempty) == 0:
            return {"pos": None, "score": 0}

        if letter == maxplayer:
            best = {"pos": None, "score": -math.inf}
        else:
            best = {"pos": None, "score": math.inf}

        for move in currempty:
            state.setingrid(move[0], move[1], letter)
            simscore = self.minimax(state, otherplayer)  
            state.setingrid(move[0], move[1], " ")      
            simscore = {"pos": move, "score": simscore["score"]}

            if letter == maxplayer:
                if simscore["score"] > best["score"]:
                    best = simscore
            else:
                if simscore["score"] < best["score"]:
                    best = simscore

        return best

    def move(self, board):
        temp = board.getemptyslots()
        if len(temp) == 9:
            posi, posj = choice(temp) 
        else:
            posi, posj = self.minimax(board, self.letter)["pos"]
        board.setingrid(posi, posj, self.letter)