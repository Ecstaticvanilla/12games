"""Guess random number chosen by the computer"""

import random

def floorlog(a,b):
    count = 1
    while a > 0:
        a = a//b
        count += 1
    return count

def guess(x):
    n = random.randint(0,x)
    choice = 100000
    count = 0
    while (n != choice):
        count += 1
        choice = int(input(f"Guess a number from 1 to {x} : "))
        if choice > n:
            print("Your choice is higher than my number!!!")        
        if choice < n:
            print("Your choice is lower than my number!!!")
    print("Yayyy!! u finally guessed it....")
    print(f"Number of tries = {count}")

def computer_guess(x):
    count  = floorlog(x,2)
    print(f"I bet i can guess your number in less than {count} tries ;)")
    low = 0
    high = x
    choice = None
    while (count > 0 or low != high):
        count -= 1
        guess = (low + high)//2
        print(f"My guess is {guess}")
        choice = input("type 'c' if correct 'h' if higher than your number or 'l' if lower than your number : ")
        if choice == "c":
            if count != 0:
                print(f"I still had {count} tries left :)")
            else:
                print("Almost had me :?")
            return
        elif choice == "h":
            high = guess
        elif choice == "l":
            low = guess        
        else:
            print("play correctly please >,<")
            count += 1
    print("I LOST!! u must have cheated ;/")

def main():
    choice = int(input("Do u want to guess(1) or the computer has to guess(2) : "))
    if(choice == 1):
        guess(1000)
    elif(choice == 2):
        x = 1000
        print(f"OK ! think of a number from 1 to {x}")
        computer_guess(x)
    else:
        print("OK dont play!!")
if __name__ == "__main__":
    main()