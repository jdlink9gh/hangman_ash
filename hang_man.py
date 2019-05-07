import random


class Hangman:

    def hm(self):
        with open("sowpods.txt") as file:
            while True:
                new_list = []
                max_len = input('Enter character max limit: ')
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

def main():
    if __name__ == "__main__":
        main()