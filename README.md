# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


## Description
The Hangman Python Project is a classic word-guessing game where the player attempts to guess a hidden word one letter at a time. The aim of this project is to create an interactive and entertaining game while practicing and improving your Python programming skills. This project is also an excellent opportunity to understand and implement concepts like input handling, random word selection, and game logic. This code developes the understanding for using classes along side OOP to generate code with a good flow and simplistic struture to allow the user a good understanding of the project.

## Installation
To run the Hangman game on your local machine, follow these installation instructions:
1. Make sure you have Python installed on your system. If not, download and install Python from [python.org](https://www.python.org/).
2. Clone this repository to your local machine or download the ZIP file and extract it.
3. Open your terminal or command prompt.
4. Navigate to the project directory.
5. Open the designated file for the game.

## Usage Instructions
To play the game of hangman:
1. A random word is chosen after the code is run.
2. The user would input a letter as their 'Guess'.
3. The input would be checked if it is a valid input such as being in the alphabet and is a single letter.
4. The guess is then analysed against the word to determine whether it was a correct guess displaying a message to confirm or an incorrect guess showing a message to try again and losing a life.
5. In the instance of it being correct it is added to the list of blanks to show how many letters left.
6. Then the turn is repeated either asking for a new letter to complete the word or showing that the user has guessed the wrong letter reducing the life points.
7. Once the game has ended the user would have either run out of lives, in that case losing, or guessed the word, in that case winning the game.

## File Structure
hangman/
    ├── hangman
    └── hangman_Template.py
├── .gitignore
├── milestone_2.py
├── milestone_3.py
├── milestone_4.py
└── README.md