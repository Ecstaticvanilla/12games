"""Rock Paper Scissors"""
import random

def win(a,b):
    if (a == "r" and b == "s") or (a == "s" and b == "p") or (a == "p" and b == "r"):
        return True
    return False

def computer_play():
    computer_choice = random.choice(['r','p','s'])
    user_choice = input("choose between rock(r), paper(p), scissors(s) ==> ")
    print("Computer == >", computer_choice)
    if computer_choice == user_choice:
        print("Tied!!")
    elif win(user_choice,computer_choice):
        print("You won congratulations!!<3")
    else:
        print("U lost :(  better luck next time")

def main():
    computer_play()

if __name__ == "__main__":
    main()