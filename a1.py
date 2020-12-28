#!/usr/bin/env python
# coding: utf-8



"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{user.name}} ({{user.id}})"
__email__ = ""
__date__ = ""


def select_word_at_random(word_select: str)-> str:
    '''Given the word select is either "FIXED" or "ARBITRARY" this function will return a string randomly 
    selected from WORDS FIXED.txt or WORDS ARBITRARY.txt respectively. If word select is anything other 
    then the expected input then this function should return None.'''
    
    if word_select == "FIXED" or word_select == "ARBITRARY":
        words = load_words(word_select)
        word_index = random_index(words)
        return words[word_index]
    else:
        return None


def guess_range(guess_no: int, word_length: int)->int:
    '''This function returns the start_index and end_index to guess.'''
    
    guess_tuple = GUESS_INDEX_TUPLE[word_length-6][guess_no-1]
    return guess_tuple[0], guess_tuple[1]


def create_guess_line(guess_no: int, word_length: int)-> str:
    '''This function returns the string representing the display corresponding to the guess number integer, guess_no.
    i.e. create_guess_line(2, 9): return 'Guess 2| - | * | * | * | - | - | - | - | - |' '''
    
    start_index, end_index = guess_range(guess_no, word_length)
    STAR = "*"
    
    guess_line = "Guess "+str(guess_no)+WALL_VERTICAL
    for i in range(word_length):
        if start_index <= i <= end_index:
            guess_line += " "+ STAR+ " "+ WALL_VERTICAL
        else:
            guess_line += " "+ WALL_HORIZONTAL+ " "+ WALL_VERTICAL
    return guess_line


def create_first_line(word_length: int)-> None:
    '''This function create the first line for the guess matrix.
    i.e. create_first_line(8): print '       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |' '''
    
    seven_space = "\040" * 7
    print("{}{}".format(seven_space, WALL_VERTICAL), end="")
    for i in range(word_length):
        print("", i+1, WALL_VERTICAL, end="")


def create_underscore(word_length: int)-> None:
    '''This function prints the underscore for the guess matrix according to word_length.
    i.e. create_underscore(8): print '-----------------------------------------' '''
    
    print('\n',end="")
    for i in range(9+4*word_length):
        print("-", end="")
    print('\n',end="")


def display_guess_matrix(guess_no: int, word_length: int, scores: tuple())-> None:
    '''This function prints the progress of the game. This includes all line strings for guesses up to guess no with
    their corresponding scores (a tuple containing all previous scores), and the line string for guess no (without
    a score).
    i.e. display_guess_matrix(3, 9, (1, 1, 2)): print the matrix below:
           | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
    ---------------------------------------------
    Guess 1| * | * | - | - | - | - | - | - | - |   1 Points
    ---------------------------------------------
    Guess 2| - | * | * | * | - | - | - | - | - |   1 Points
    ---------------------------------------------
    Guess 3| - | - | - | - | * | * | * | * | - |
    ---------------------------------------------
    '''
    
    three_space = "\040" * 3
    create_first_line(word_length)
    create_underscore(word_length)
    for i in range(guess_no):
        print(create_guess_line(i+1, word_length), end="")
        if i<guess_no-1:
            print("{}{} Points".format(three_space, scores[i]), end="")
        create_underscore(word_length)


def compute_value_for_guess(word: str, start_index: int, end_index: int, guess: str)-> int:
    '''Return the score, an integer, the player is awarded for a specific guess. The word is a string representing the
    word the player has to guess. The substring to be guessed is determined by the start_index and end_index.
    The substring is created by slicing the word from the start_index up to and including the end_index. The
    guess is a string representing the guess attempt the player has made.'''
    
    point = 0
    for i in range(start_index, end_index+1):
        if guess[i-start_index] == word[i]:  #correct letter in the correct position
            if guess[i-start_index] in VOWELS:
                point += 14
            else:  #CONSONANTS
                point += 12
        elif guess[i-start_index] in word[start_index:end_index+1]:  #letter guessed correctly but in the wrong position
            point += 5
    return point


def game_control()-> None:
    '''This function prints the game flow guide and controls the progress of the game flow.'''
    
    level_query = "Do you want a 'FIXED' or 'ARBITRARY' length word?: "
    start_now = "Now try and guess the word, step by step!!"
    guess_enter = "Now enter Guess "
    final_enter = "Now enter your final guess. i.e. guess the whole word: "
    win = "You have guessed the word correctly. Congratulations."
    lose = "Your guess was wrong. The correct word was"

    scores = [0]  #set a list to save the scores
    
    #select the word
    word_select = None
    while word_select not in ('FIXED', 'ARBITRARY'): #check if the input is valid
        word_select = input(level_query)
    word = select_word_at_random(word_select)
    word_length = len(word)
    
    #start guess
    print(start_now)
    for guess_no in range(1, word_length+1):
        display_guess_matrix(guess_no, word_length, tuple(scores))
        guess = ""
        start_index, end_index = guess_range(guess_no, word_length)
        while len(guess)!=end_index-start_index+1:  #check the input string length
            if guess_no != word_length:
                guess = input(guess_enter+str(guess_no)+": ")
            else:
                guess = input(final_enter)  #last guess
        point = compute_value_for_guess(word, start_index, end_index, guess)
        scores[guess_no-1] = point
        scores.append(0)
    if guess == word:
        print(win)
    else:
        print("{} \"{}\"".format(lose, word))


def main():
    """
    Handles top-level interaction with user.
    """
    # Write the code for your main function here
    print(WELCOME)
    action = input(INPUT_ACTION)
    while action not in ("s", "h", "q"):
        action = input(INVALID+'\n'+INPUT_ACTION)
    if action=="s":
        game_control()
    elif action=="h":
        print(HELP)
        game_control()
    else:
        return

if __name__ == "__main__":
    main()