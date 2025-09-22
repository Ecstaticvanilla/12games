from board import Board
from player import Computer,Player,GoodComputer
from time import sleep

def choiceplayer(choice, letter):
    if choice == "1":
        return Player(letter)
    elif choice == "2":
        return Computer(letter)    
    elif choice == "3":
        return GoodComputer(letter)

def tictactoe(player1,player2,board):
    for i in range(9):
        if i%2 == 0:
            player1.move(board)
        else:
            player2.move(board)
        sleep(2)
        board.printgrid()
        winningletter ,isWin = board.isWin()
        if isWin:
            print(f"'{winningletter}' Won")
            return
    print("Its a DRAW!! wow")


def main():
    board = Board()
    board.printgrid()

    input1 = input("Enter user(1) or computer(2) or unbeatablecomputer(3) as player1 --> ")
    input2 = input("Enter user(1) or computer(2) or unbeatablecomputer(3) as player2 --> ")

    player1 = choiceplayer(input1,"X")
    player2 = choiceplayer(input2,"O")

    # print(type(player1))
    # print(type(player2))
    tictactoe(player1,player2,board)

if __name__ == "__main__":
    main()

