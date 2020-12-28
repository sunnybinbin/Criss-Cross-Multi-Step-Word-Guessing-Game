"""
CSSE1001 Assignment 1 Support Code - You do not need to copy/paste this.
All code is available via the line already supplied in a1.pt

from a1_support import *

"""

import random


GUESS_INDEX_TUPLE = (
    ((0, 1), (2, 4), (2, 4), (3, 5), (2, 5), (0, 5)),                         # word length 6
    ((0, 1), (1, 2), (4, 6), (2, 5), (3, 6), (2, 6), (0, 6)),                 # word length 7
    ((0, 1), (1, 3), (4, 7), (3, 5), (3, 6), (5, 7), (2, 7), (0, 7)),         # word length 8
    ((0, 1), (1, 3), (4, 7), (3, 5), (3, 6), (5, 7), (3, 7), (2, 8), (0, 8))  # word length 9
)

WALL_VERTICAL = "|"
WALL_HORIZONTAL = "-"

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

WELCOME = """
Welcome to the Criss-Cross Multi-Step Word Guessing Game!
"""

INPUT_ACTION = """
Enter an input action. Choices are:
s - start game
h - get help on game rules
q - quit game: 
"""

HELP = """
Game rules - You have to guess letters in place of the asterixis. 
Each vowel guessed in the correct position gets 14 points. 
Each consonant guessed in the correct position gets 12 points. 
Each letter guessed correctly but in the wrong position gets 5 points. 
If the true letters were "dog", say, and you guessed "hod", 
you would score 14 points for guessing the vowel, "o", in the correct 
position and 5 points for guessing "d" correctly, but in the 
incorrect position. Your score would therefore be 19 points.
"""

INVALID = """
Please enter a valid command.
"""


def load_words(word_select):
    """
    Loading in the selection of words from either the FIXED or ARBITRARY word
    length.

    Parameters:
        word_select (str): "FIXED" or "ARBITRARY" word sets.
    Returns:
        (tuple<str>): A tuple containing all the words.
    """
    with open(f"WORDS_{word_select}.txt", "r") as file:
        file_contents = file.read()

    words = file_contents.splitlines()
    return tuple(words)


def random_index(words):
    """
    Returns an int representing the index for the word to be guessed.

    Parameters:
        words (tuple<str>): tuple of word strings to take an index from

    (int): The randomly selected index corresponding to a word string in words
    """
    return random.randrange(0, len(words))
