from board import Board

def main():
    #create board
    x = input("Small(s) , Medium(m), High(h) : ")
    size = 8
    if x == "m":
        size = 10
    elif x == "h":
        size = 12 
    board = Board(size)
    flags = board.createboard()
    board.printboard(debug=True)

    # Game Loop
    while True:
        print(f"{flags} Flags Left")
        board.printboard()
        choice = input(f"Dig(1) or Flag(2) : ")

        i,j = map(int,input(f"Enter coordinate(1 indexed) : ").split())
        i -= 1
        j -= 1

        if choice == "1":
            mine = board.dig(i,j)
            if mine:
                print("YOU LOST!!! L (Better luck next time)")
                board.printboard(debug=True)
                break
        
        elif choice == "2":
            if flags == 0:
                print("No flags left")
            else:
                flags += board.flag(i,j)

        if board.isWin():
            print("YOU WON!!!!!!!")
            break

if __name__ == "__main__":
    main()