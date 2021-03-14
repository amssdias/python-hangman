import random
from typing import List

def guessing_game(word: List, number_letters: int):
    # Give one random letter
    letters = list(random.sample(word, k=number_letters))

    guesses = 0
    while True:
        print()

        if guesses == 6:
            print(f"Sorry, you lost, the word was: {word.upper()}!")
            exit(0)

        answer = []

        # Display word
        for x in word:
            for i in letters:
                if i == x:
                    print(i, end=" ")
                    answer.append(i)
                    break
            else:
                print("_", end=" ")

        # Check if user guessed the word
        if "".join(answer) == "".join(word):
            print("\nCongratulations, you won!")
            exit(0)

        # User choose letter
        print(f'''
                Letters used: {" | ".join(letters)}
                Guesses Left: {guesses} ''')
        new_letter = input("Choose new letter: ")

        if new_letter not in letters:
            letters.append(new_letter)
            letters.sort()

        if new_letter not in word:
            guesses += 1