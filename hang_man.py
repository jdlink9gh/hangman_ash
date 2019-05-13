import os
import sys
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
            |‾‾‾‾‾‾‾‾|
            |     O
            |   
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾‾|
            |     O
            |    /
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾‾|
            |     O
            |    /|
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾‾|
            |     O
            |    /|\\
            |   
            |
            """,
            """
            |‾‾‾‾‾‾‾‾|
            |     O
            |    /|\\
            |    / 
            |
            """,
            """
            |‾‾‾‾‾‾‾‾|
            |     O
            |    /|\\
            |    / \\
            |
            """]

    def access_doc(self):
        url = 'http://norvig.com/ngrams/sowpods.txt'  # Create a variable that stores for URL for text file
        file_exist = os.path.exists('./word_folder/sowpods.txt')  # Boolean value to check if text file exist first
        if not file_exist:  # If text file does not exist following happens:
            folder_exist = os.path.isdir('./word_folder/')  # Checks to see if directory exists
            if not folder_exist:  # If directory does not exist following happens:
                os.mkdir('./word_folder/')  # Creates the directory
                word_file = urllib.request.urlretrieve(url, './word_folder/sowpods.txt')  # Download word file into dir
                return os.path.relpath(word_file[0])  # Returns path
            else:  # if dir already exists
                word_file = urllib.request.urlretrieve(url, './word_folder/sowpods.txt')  # Download word file into dir
                return os.path.relpath(word_file[0])  # Returns path
        else:
            return os.path.relpath('./word_folder/sowpods.txt')  # Returns path if file already exists

    def assign_word(self):
        empty_list = []
        text_file = self.access_doc()
        with open(text_file) as file:
            self.word_list = file.read().splitlines()
            for word in self.word_list:
                if len(word) >= self.min_limit:
                    empty_list.append(word)
                    right_word = random.choice(empty_list)
            return right_word

    def hangman_game(self):
        correct_word = self.assign_word()
        self.right_list = list(correct_word)
        right = 0
        wrong = 0
        selected = []
        random_string = ''.join(string.ascii_uppercase)
        random_list = list(random_string)

        blank_list = ["__"] * len(self.right_list)

        while wrong != 6 and right != len(self.right_list):
            print('For testing validation, right word is: ' + correct_word)
            print(self.hang_list[wrong])
            print('Pick from these letters: ' + ' '.join(random_list))
            print('Current status: ' + ' '.join(blank_list))
            guess_letter = input('Guess a letter: ').upper()
            if guess_letter not in random_list:
                print('PLEASE PICK A CHARACTER FROM THE LIST PROVIDED')
            elif guess_letter in selected:
                print('ALREADY USED THAT CHARACTER ONCE')
            elif guess_letter in self.right_list:
                selected.append(guess_letter)
                word_pos = [pos for pos, char in enumerate(correct_word) if char == guess_letter]
                j = 0
                while j != len(word_pos):
                    blank_list[word_pos[j]] = guess_letter
                    j += 1
                right = right + j
                x = random_list.index(guess_letter)
                random_list[x] = '~~'
                print('RIGHT SELECTION')
            else:
                selected.append(guess_letter)
                x = random_list.index(guess_letter)
                random_list[x] = '~~'
                wrong += 1
                print('WRONG SELECTION')
        if right == len(self.right_list):
            print('Current status: ' + ' '.join(blank_list))
            print('YOU WON! The correct word was: ' + correct_word)
            sys.exit()
        else:
            print(self.hang_list[6])
            print('Sorry you loose, the correct word was: ' + correct_word)
            sys.exit()


def main():
    parser = argparse.ArgumentParser(description='Hangman Game')
    parser.add_argument('-m', '--min_limit', type=int, metavar='', required=True,
                        help='Enter minimum length of word ')
    args = parser.parse_args()
    game = Hangman(args.min_limit)
    game.hangman_game()


if __name__ == '__main__':
    main()
