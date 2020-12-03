# Day 7 of 100 Days of Coding Challenge

# Steps
# Generate random word
# Generate as many blanks as characters in the word
# Ask the player to choose a letter
# Is the letter in the word - Yes. Replace the blank with the letter. No. Draw a line. Have they run out of guesses- Yes- you lose. No-Ask the player to guess a letter
# Are all blanks filled - No. Ask player to guess a letter. Yes_ You win
# TODO remove the chosen word from the list

import random
word_list = ["dedication", "unicorn", "papaya", "aerodynamic", "saddle"]

chosen_word = random.choice(word_list)
print(chosen_word)
display = []

for x in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Guess a letter\n").lower()


for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)


