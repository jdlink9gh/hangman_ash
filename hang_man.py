import random
import string

class Hangman:

    def hm(self):
        with open("sowpods.txt") as file:
            while True:
                new_list = []
                max_len = input('Enter max character limit: ')
                if not max_len.isdigit():
                    print('Please enter a number')
                    continue
                else:
                    int_len = int(max_len)
                    word_list = file.read().splitlines()
                    for word in word_list:
                        if len(word) <= int_len:
                            new_list.append(word)
                            right_word = random.choice(new_list)
                            right_list = list(right_word)

                            random_string = ''.join(random.choice(string.ascii_letters) for x in range(5)) + right_word
                            guess_string = ''.join(random.sample(random_string, len(random_string)))
                            random_list = list(guess_string.upper())

                    blank_list = ["__"] * len(right_list)
                    print(right_list)
                    right = 0
                    wrong = 0
                    hang_list = [
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
                    while wrong != 6:
                        print(hang_list[wrong])
                        print('Pick from these letters: ' + ' '.join(random_list))
                        print('Current status: ' + ' '.join(blank_list))
                        guess_word = input('Guess a letter: ')
                        if guess_word.upper() in right_list:
                            right += 1
                            print('RIGHT SELECTION')
                        else:
                            print('WRONG SELECTION')
                            wrong += 1
                    print(hang_list[6])
                    print("Sorry you loose, the correct word was: " + right_word)
                    break

def main():
    if __name__ == "__main__":
        main()
