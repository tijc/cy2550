# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:10:01 2023

@author: tijana
"""

# shebang syntax for the python interpreter
#!/usr/bin/env python3

# imports all necessary packages
import sys
import random
import string

def generate_password(words, caps, numbers, symbols):
    """ generates a random secure password using the XKCD method """
    
    # reads the list of words to choose words from
    with open('words.txt') as f:
        words_list = f.read().splitlines()

    # checks to make sure there is enough words to create the password
    if words > len(words_list):
        print("not enough words to generate the password!")
        return ""

    # gets a set of random words equal to the number of words chosen to use
    random_words = random.sample(words_list, words)

    # if the number of words the user wants to capitalize is larger than the
    # number of words in the password, then creates a best-effort password and
    # capitalizes as many words as it can (the number of words in the password)
    if caps > words:
        caps = words

    # capitalizes a certain number of random words based on the user's choice
    words_to_capitalize = random.sample(range(words), caps)
    password_words = []
    
    for i, word in enumerate(random_words):
        if i in words_to_capitalize:
            password_words.append(word.capitalize())
        else:
            password_words.append(word)
    
    # adds random numbers to each word if the user wants to add numbers
    for _ in range(numbers):
        random_word_index = random.randint(0, words - 1)
        random_number = random.choice(string.digits)
        password_words[random_word_index] += random_number

    # adds random symbols to each word if the user wants to add symbols
    for _ in range(symbols):
        random_word_index = random.randint(0, words - 1)
        random_symbol = random.choice(string.punctuation)
        password_words[random_word_index] += random_symbol

    # concatenates all of the words at the end to form the final password
    password = ''.join(password_words)

    # returns the final secure password
    return password
   
def print_help():
    """ prints out the help message """
    
    print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]")
    print("\nGenerate a secure, memorable password using the XKCD method")
    print("\noptional arguments:")
    print("  -h, --help            show this help message and exit")
    print("  -w WORDS, --words WORDS")
    print("                        include WORDS words in the password (default=4)")
    print("  -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words")
    print("                        (default=0)")
    print("  -n NUMBERS, --numbers NUMBERS")
    print("                        insert NUMBERS random numbers in the password")
    print("                        (default=0)")
    print("  -s SYMBOLS, --symbols SYMBOLS")
    print("                        insert SYMBOLS random symbols in the password")
    print("                        (default=0)")
    
def main():
    
    # takes in the arguments given by the user in the command line
    args = sys.argv[1:]
    
    # checks if the user inputted "-h" or "--help" as an argument
    if ("-h" in args) or ("--help" in args):
        print_help()
        return
    
    # sets the argument values
    words = 4
    caps = 0
    numbers = 0
    symbols = 0

    # checks for what the user inputs in the command line and updates the
    # corresponding values accordingly
    for i in range(len(args)):
        if (args[i] == "-w" or args[i] == "--words") and i + 1 < len(args):
            words = int(args[i + 1])
        elif (args[i] == "-c" or args[i] == "--caps") and i + 1 < len(args):
            caps = int(args[i + 1])
        elif (args[i] == "-n" or args[i] == "--numbers") and i + 1 < len(args):
            numbers = int(args[i + 1])
        elif (args[i] == "-s" or args[i] == "--symbols") and i + 1 < len(args):
            symbols = int(args[i + 1])

    # generates a random secure password using the XKCD method
    password = generate_password(words, caps, numbers, symbols)
    print(password)

if __name__ == "__main__":
    main()
