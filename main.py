# Day 7 of 100 Days of Coding Challenge

# TODO clear function not working


import random
from word_list import *
from artwork import *
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


game_over = False
chosen_word = random.choice(word_list)
lives = 6
display = []
print(logo)
for x in range(len(chosen_word)):
    display += "_"
print(f"{''.join(display)}")

while not game_over:
    guess = input("Guess a letter\n").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} not in answer.")
        print(f"You have {lives} guesses remaining")

        if lives == 0:
            print("You lose")
            print(f"The answer is {chosen_word}")
            game_over = True
    print(f"{''.join(display)}")
    if "_" not in display:
        game_over = True
        print("You win!")
    print(stages[lives])
