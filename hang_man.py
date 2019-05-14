import os
import sys
import copy
import string
import random
import argparse
import urllib.request


class Hangman:

    def __init__(self, min_limit):  # Creating init method that takes in max word limit as perimeter
        self.min_limit = min_limit  # Minimum word limit taken from user
        self.word_list = []  # A list that stores all the word from local file or web
        self.right_list = []  # A list that stores the right word
        self.guess_letter = str  # User input of their guessed character
        self.hang_list = [       # A list that contains all the stages of hangman
            """
            |‾‾‾‾‾‾‾‾|
            |       
            |      
            |      
            |
            """,
            """
            |‾‾‾‾‾‾‾|
            |       O
            |   
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾|
            |       O
            |      /
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾|
            |       O
            |      /|
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾|
            |       O
            |      /|\\
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾|
            |       O
            |      /|\\
            |      / 
            |
            """,
            """
            |‾‾‾‾‾‾‾|
            |       O
            |      /|\\
            |      / \\
            |
            """]

    def access_doc(self):
        url = 'http://norvig.com/ngrams/sowpods.txt'  # Create a variable that stores for URL for text file
        file_exist = os.path.exists('./word_data/words.txt')  # Boolean value to check if text file exist first
        if not file_exist:  # If text file does not exist following happens:
            folder_exist = os.path.isdir('./word_data/')  # Checks to see if directory exists
            if not folder_exist:  # If directory does not exist following happens:
                os.mkdir('./word_data/')  # Creates the directory
                word_file = urllib.request.urlretrieve(url, './word_data/words.txt')  # Download word file into dir
                return os.path.relpath(word_file[0])  # Returns path
            else:  # if dir already exists
                word_file = urllib.request.urlretrieve(url, './word_data/words.txt')  # Download word file into dir
                return os.path.relpath(word_file[0])  # Returns path
        else:
            return os.path.relpath('./word_data/words.txt')  # Returns path if file already exists

    def assign_word(self):
        empty_list = []
        text_file = self.access_doc()           # Getting text file location from previous method
        with open(text_file) as file:           # Opening text file
            self.word_list = file.read().splitlines()       # Reading text files and splitting word
            for word in self.word_list:         # Loop to iterate through all the words in file
                if len(word) >= self.min_limit:         # Finding all words that are greater than or equal to min limit
                    empty_list.append(word)         # All the words are being added to empty list
                    right_word = random.choice(empty_list)      # From that list program randomly selects a random word
            return right_word           # Returns the random word

    def hangman_game(self):
        correct_word = self.assign_word()       # Getting the word selected by program from previous method
        self.right_list = list(correct_word)        # Converting the word into a list
        right = 0                       # Counter to keep track of right word guessed
        wrong = 0               # Counter to keep track of wrong word guessed
        selected = []           # A list that keeps track of all the letter selected by user
        random_string = ''.join(string.ascii_uppercase)     # Getting characters from A - Z
        random_list = list(random_string)               # Converting the characters into list
        temp_rlist = copy.deepcopy(random_list)         # making a temporary copy of the characters list

        blank_list = ["__"] * len(self.right_list)      # A list is created with __ to show user status of word

        while wrong != 6 and right != len(self.right_list):   # loop that executes until user guess right word/looses
            print('For testing validation, right word is: ' + correct_word)  # Printing the right word for validation
            print(self.hang_list[wrong])                            # Print the first stage of hangman
            print('Pick from these letters: ' + ' '.join(random_list))  # Displays characters A-Z for user to pick from
            print('Current status: ' + ' '.join(blank_list))        # Displays the current status of word by using __
            guess_letter = input('Guess a letter: ').upper()        # Asks the user to input in one character
            if not guess_letter.isalpha():                    # if the char is not string value it will provide an error
                print('Please enter a string character')
            elif len(guess_letter) != 1:            # If user does not input only one char it will provide an error
                print('Enter one character only')
            elif guess_letter not in temp_rlist:      # If the guessed letter is not from A-Z it will provide an error
                print('PLEASE PICK A CHARACTER FROM THE LIST PROVIDED')
            elif guess_letter in selected:      # If the user input a char they already used it provides an error
                print('ALREADY USED THAT CHARACTER ONCE')
            elif guess_letter in self.right_list:  # If user selects a char that is in right word list
                selected.append(guess_letter)       # Selected word list is updated
                word_pos = [pos for pos, char in enumerate(correct_word) if char == guess_letter]
                # Find the position to see how many time a guessed char repeats within the correct word
                j = 0
                while j != len(word_pos):  # The guessed char is replace in the same index value of blank list
                    blank_list[word_pos[j]] = guess_letter
                    j += 1
                right = right + j       # Updating right guessed counter
                x = random_list.index(guess_letter)   # Finds the index value of guessed char within random list (A-Z)
                random_list[x] = '~~'               # Updates the random list so user knows which char to pick from
                print('RIGHT SELECTION')        # Print statement to inform user that they have guessed correct char
            else:
                selected.append(guess_letter)  # Select list is updated so user can not pick the same char again
                x = random_list.index(guess_letter)  # Finds the index value of guessed char within random list (A-Z)
                random_list[x] = '~~'    # Updates the random list so user knows which char to pick from
                wrong += 1              # Updating wrong guessed counter
                print('WRONG SELECTION')    # Print statement to inform user that they have guessed wrong char
        if right == len(self.right_list):   # If right counter matches length of right word
            print('Current status: ' + ' '.join(blank_list))   # Shows current status of word
            print('YOU WON! The correct word was: ' + correct_word)         # Informs user that they have won
            sys.exit()          # Exists the program
        else:   # When the counter reaches 6, last stage of hangman
            print(self.hang_list[6])    # Prints the lat stage of hangman
            print('Sorry you loose, the correct word was: ' + correct_word)    # Shows the correct word
            sys.exit()          # Exists the program


def main():             # Driver function
    parser = argparse.ArgumentParser(description='Hangman Game')
    parser.add_argument('-m', '--min_limit', type=int, metavar='', required=True,
                        help='Enter minimum length of word ')
    args = parser.parse_args()
    game = Hangman(args.min_limit)      # Creates game object out of class
    game.hangman_game()         # Starts the game function


if __name__ == '__main__':      # Calling main function
    main()
