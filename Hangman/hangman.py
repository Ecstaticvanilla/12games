"""Hangman"""

import random
import json

with open("words.json", "r", encoding="utf-8") as file:
    words = json.load(file)

def hangman():
    word = random.choice(words['data'])


    guessset = set([])

    lives = 9
    correctletters = len(word)

    while(lives > 0):
        print(*guessset)
        lives -= 1
        while True:
            choice = input("Enter your choice : ")
            if not choice.isalpha() or choice in guessset:
                print("Please enter valid .. ")
            else:
                break
        guessset.add(choice)
        if choice in word:
            correctletters -= 1
        if correctletters == 0:
            print("YOU are correct !!! You won!! congrats")
            break
        print(*[i  if i in guessset else "_" for i in word])

    print(f"You Lost the word was '{word}'")

def main():
    hangman()

if __name__ == "__main__":
    main()