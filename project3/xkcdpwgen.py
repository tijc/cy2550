# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:10:01 2023

@author: tijana
"""

#!/usr/bin/env python3

import sys
import random
import string
from random import randint

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
    #password = ''.join(password_words)

    #password_length = len(password)

    # Create the concatenated string with spaces between words
    concatenated_string = ' '.join(password_words)

    # # Get all possible positions to insert numbers and symbols (at word boundaries)
    # possible_positions = [i * 2 for i in range(words + 1)]

    # # Insert numbers
    # if numbers:
    #     for _ in range(numbers):
    #         random_position = random.choice(possible_positions)
    #         random_number = random.choice(string.digits)
    #         concatenated_string = concatenated_string[:random_position] + random_number + concatenated_string[random_position:]

    # # Insert symbols
    # if symbols:
    #     for _ in range(symbols):
    #         random_position = random.choice(possible_positions)
    #         random_symbol = random.choice(string.punctuation)
    #         concatenated_string = concatenated_string[:random_position] + random_symbol + concatenated_string[random_position:]

    # Insert numbers at the beginning or end
    for _ in range(numbers):
        if random.choice([True, False]):
            random_number = random.choice(string.digits)
            concatenated_string = random_number + concatenated_string
        else:
            random_number = random.choice(string.digits)
            concatenated_string = concatenated_string + random_number
    
    # Insert symbols at the beginning or end
    for _ in range(symbols):
        if random.choice([True, False]):
            random_symbol = random.choice(string.punctuation)
            concatenated_string = random_symbol + concatenated_string
        else:
            random_symbol = random.choice(string.punctuation)
            concatenated_string = concatenated_string + random_symbol

    return concatenated_string

    #return concatenated_string.replace(" ", "")  # Remove spaces to get the final password
    
def insert_number_or_symbol(input_string, character):
    # Split the input string into words
    words = input_string.split()

    # Choose a random word from the list
    random_word_index = random.randint(0, len(words) - 1)
    chosen_word = words[random_word_index]

    # Generate a random position index within the chosen word
    random_index = random.randint(0, len(chosen_word))

    # Insert the character (number or symbol) at the chosen position
    modified_word = chosen_word[:random_index] + character + chosen_word[random_index:]

    # Replace the original word with the modified word
    words[random_word_index] = modified_word

    # Join the words back together to form the new string
    new_string = ' '.join(words)

    return new_string

def main():
    
    args = sys.argv[1:]
    
    words = 2
    caps = 0
    numbers = 2
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

    # # Example usage:
    # original_string = "thisisateststring"
    # modified_string = insert_number_or_symbol(original_string, '7')
    # print(modified_string)

if __name__ == "__main__":
    main()
