import random



class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(self.word_guessed)

    def check_letter(self, letter):
        '''
        Initializes the Hangman game with a random word from the word list.

        Args:
            word_list (list): List of words to choose from.
            num_lives (int): Number of lives the player has (default is 5).

        Initializes the game state, including the selected word, word_guessed, and list_of_guesses.
        '''
        letter = letter.lower()
        if letter in self.word:
            print(f'Good guess! {letter} is in the word.')
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''
         Ask the user to guess a letter and handle invalid input.

        Continuously prompts the user for input until a valid letter is provided.

        '''
        while True:
            letter = input('Enter a single letter: ')
            if len(letter) != 1 or not letter.isalpha():
                print(f'Invalid letter. Please enter a single alphabetical character.')
            elif letter in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_letter(letter)
                self.list_of_guesses.append(letter)
            break

def play_game(word_list):
    '''
    Initialize and play the Hangman game.

    Args:
        word_list (list): List of words for the game.

    Initializes the Hangman game and manages the game flow until the player either wins or runs out of lives. 
    '''
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif (game.num_lives != 0) and (game.num_letters == 0):
            print('Congratulations. You have won the game!')
            break

if __name__ == '__main__':
    words = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(words)