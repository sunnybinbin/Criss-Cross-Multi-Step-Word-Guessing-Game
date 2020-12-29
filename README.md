# Criss-Cross-Multi-Step-Word-Guessing-Game
## Background
The goal of the game is for the player to guess that word through a series of guesses of "subwords". The player will have a different number of guesses (with different subwords to guess) depending on the difficulty selection. If the player chooses the "FIXED" difficulty, a eight-letter word will be guessed. If the player chooses the "ARBITRARY" difficulty, a random length word will be guessed. The user give a letter in each guess, and the program will show the goal user get.
* Each vowel guessed in the correct position gets 14 points.
* Each consonant guessed in the correct position gets 12 points.
* Each letter guessed correctly but in the wrong position gets 5 points.
Take a eight-letter word for example, after seven guesses, the user is required to give the final answer, and the program will tell WIN or LOSE.
## Usage
Run a1.py to start playing.
a1_support.py, WORDS_ARBITRARY.txt, and WORDS_FIXED.txt are required for a1.py.
If the player chooses the "FIXED" difficulty, the word must be selected at random from the WORDS_FIXED.txt file. If the player chooses the "ARBITRARY" difficulty, the word must be selected at random from the WORDS_ARBITRARY.txt file.
## Test
This project comes from an assignment from CSSE1001.
Run test_a1.py for function testing.
## Appendix
### Welcome message
"Welcome to the Criss-Cross Multi-Step Word Guessing Game!
Enter an input action. Choices are:
s - start game
h - get help on game rules
q - quit game:
"
### Help message
"Game rules - You have to guess letters in place of the asterixis.
Each vowel guessed in the correct position gets 14 points.
Each consonant guessed in the correct position gets 12 points.
Each letter guessed correctly but in the wrong position gets 5 points.
If the true letters were "dog", say, and you guessed "hod",
you would score 14 points for guessing the vowel, "o", in the
correct position and 5 points for guessing "d" correctly, but in the
incorrect position. Your score would therefore be 19 points."
### Printing Example
Welcome to the Criss-Cross Multi-Step Word Guessing Game!


Enter an input action. Choices are:
s - start game
h - get help on game rules
q - quit game:
s
Do you want a 'FIXED' or 'ARBITRARY' length word?: FIXED
Now try and guess the word, step by step!!
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |
-----------------------------------------
Now enter Guess 1: ab
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |   5 Points
-----------------------------------------
Guess 2| - | * | * | * | - | - | - | - |
-----------------------------------------
Now enter Guess 2: abc
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |   5 Points
-----------------------------------------
Guess 2| - | * | * | * | - | - | - | - |   0 Points
-----------------------------------------
Guess 3| - | - | - | - | * | * | * | * |
-----------------------------------------
Now enter Guess 3: defg
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |   5 Points
-----------------------------------------
Guess 2| - | * | * | * | - | - | - | - |   0 Points
-----------------------------------------
Guess 3| - | - | - | - | * | * | * | * |   26 Points
-----------------------------------------
Guess 4| - | - | - | * | * | * | - | - |
-----------------------------------------
Now enter Guess 4: sdr
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |   5 Points
-----------------------------------------
Guess 2| - | * | * | * | - | - | - | - |   0 Points
-----------------------------------------
Guess 3| - | - | - | - | * | * | * | * |   26 Points
-----------------------------------------
Guess 4| - | - | - | * | * | * | - | - |   12 Points
-----------------------------------------
Guess 5| - | - | - | * | * | * | * | - |
-----------------------------------------
Now enter Guess 5: sedf
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |   5 Points
-----------------------------------------
Guess 2| - | * | * | * | - | - | - | - |   0 Points
-----------------------------------------
Guess 3| - | - | - | - | * | * | * | * |   26 Points
-----------------------------------------
Guess 4| - | - | - | * | * | * | - | - |   12 Points
-----------------------------------------
Guess 5| - | - | - | * | * | * | * | - |   10 Points
-----------------------------------------
Guess 6| - | - | - | - | - | * | * | * |
-----------------------------------------
Now enter Guess 6: dfg
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |   5 Points
-----------------------------------------
Guess 2| - | * | * | * | - | - | - | - |   0 Points
-----------------------------------------
Guess 3| - | - | - | - | * | * | * | * |   26 Points
-----------------------------------------
Guess 4| - | - | - | * | * | * | - | - |   12 Points
-----------------------------------------
Guess 5| - | - | - | * | * | * | * | - |   10 Points
-----------------------------------------
Guess 6| - | - | - | - | - | * | * | * |   0 Points
-----------------------------------------
Guess 7| - | - | * | * | * | * | * | * |
-----------------------------------------
Now enter Guess 7: sdrsw
Now enter Guess 7: ertfds
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
-----------------------------------------
Guess 1| * | * | - | - | - | - | - | - |   5 Points
-----------------------------------------
Guess 2| - | * | * | * | - | - | - | - |   0 Points
-----------------------------------------
Guess 3| - | - | - | - | * | * | * | * |   26 Points
-----------------------------------------
Guess 4| - | - | - | * | * | * | - | - |   12 Points
-----------------------------------------
Guess 5| - | - | - | * | * | * | * | - |   10 Points
-----------------------------------------
Guess 6| - | - | - | - | - | * | * | * |   0 Points
-----------------------------------------
Guess 7| - | - | * | * | * | * | * | * |   27 Points
-----------------------------------------
Guess 8| * | * | * | * | * | * | * | * |
-----------------------------------------
Now enter your final guess. i.e. guess the whole word: weiunfks
Your guess was wrong. The correct word was "blinders"
