# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:10:01 2023

@author: tijana
"""

#!/usr/bin/env python3

import sys
import random
import string

# Function to generate a random password using the XKCD method
def generate_password(words, caps, numbers, symbols):
    with open('words.txt') as f:
        words_list = f.read().splitlines()

    if words > len(words_list):
        print("Not enough words in the dictionary to generate the password.")
        return ""

    random_words = random.sample(words_list, words)

    if caps > words:
        caps = words

    # if numbers > words:
    #     numbers = words

    # if symbols > words:
    #     symbols = words

    # Capitalize random words
    words_to_capitalize = random.sample(range(words), caps)
    password_words = [word.capitalize() if i in words_to_capitalize else word for i, word in enumerate(random_words)]
    password = ''.join(password_words)

    if numbers:
        for num in range(numbers):
            random_index = random.randint(0, len(password) - 1)
            random_number = random.choice(string.digits)
            password = password[:random_index] + random_number + password[random_index:]

    if symbols:
        for sym in range(symbols):
            random_index = random.randint(0, len(password) - 1)
            random_symbol = random.choice(string.punctuation)
            password = password[:random_index] + random_symbol + password[random_index:]

    return password

def main():
    
    args = sys.argv[1:]
    
    words = 4
    caps = 0
    numbers = 0
    symbols = 0

    for i in range(len(args)):
        if (args[i] == "-w" or args[i] == "--words") and i + 1 < len(args):
            words = int(args[i + 1])
        elif (args[i] == "-c" or args[i] == "--caps") and i + 1 < len(args):
            caps = int(args[i + 1])
        elif (args[i] == "-n" or args[i] == "--numbers") and i + 1 < len(args):
            numbers = int(args[i + 1])
        elif (args[i] == "-s" or args[i] == "--symbols") and i + 1 < len(args):
            symbols = int(args[i + 1])

    password = generate_password(words, caps, numbers, symbols)
    print(password)

if __name__ == "__main__":
    main()
