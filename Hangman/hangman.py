import random
from sys import exit

from game_logic import guessing_game

words = [
    'lion', 'elephant', 'word', 'programming', 
    'technology', 'hangman', 'jazzy', 'whiskey', 
    'wizard'
    ]

word = random.choice(words)
word_lenght = len(word)

# Difficulty of game
if word_lenght <= 4:
    guessing_game(word=word, number_letters=1)
elif word_lenght <= 6:
    guessing_game(word=word, number_letters=2)
elif word_lenght <= 8:
    guessing_game(word=word, number_letters=3)
else:
    guessing_game(word=word, number_letters=4)
