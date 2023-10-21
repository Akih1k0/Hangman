import random
# Created fruit list
word_list = ['Apple', 'Banana', 'Pear', 'Kiwi', 'Grape']
print(word_list)
# Choose random word from list
word = random.choice(word_list)
print(word)
# Input to guess a letter
guess = input('Enter a single letter: ')
# Checks if the letter is a single letter and in the alphabet
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input')
