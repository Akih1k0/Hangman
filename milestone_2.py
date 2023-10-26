import random

def random_word():

    word_list = ['Apple', 'Banana', 'Pear', 'Kiwi', 'Grape', 'Cherry']
    word = random.choice(word_list)
    print(word)

def guess_input():

    guess = input('Enter a single letter: ')
    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
    else:
        print('Oops! That is not a valid input')

random_word()
guess_input()