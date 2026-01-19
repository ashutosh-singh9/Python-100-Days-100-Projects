# Break the problem

# Part 1
# generate a random word each time, take input of letter, if that letter exist in random word print true at that place else false 

import random as rd
words = ["apple","bottle","mouse"]

chosen_word = rd.choice(words)

print(chosen_word)


guessed_letter = input("Enter the Guessed word: ")

for i in range(len(chosen_word)):
    # print (chosen_word[i])
    if guessed_letter == chosen_word[i]:
        print("True")
    else:
        print("False")