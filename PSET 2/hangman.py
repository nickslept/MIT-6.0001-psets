#pset 2 - hangman; REMEMBER TO CHECK THE COMMIT BEFORE 3/6 11:SOMETHING AM TO FIND THE CODE THAT WAS DELETED TEMPORARILY BELOW THE HANGMAN FUNCTION

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    c = 0
    for char in secret_word:
        if char in letters_guessed:
            c+=1
    if c == len(secret_word):
        return True
    return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    s = ""
    for char in secret_word:
        if char in letters_guessed:
            s+=char
        else:
            s+="_ "
    return s



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = list(string.ascii_lowercase)
    for e in letters_guessed:
        letters_not_guessed.remove(e)
    return("".join(letters_not_guessed))

def check_and_give_warning(guess, letters_guessed, warnings_left):
    if not str.isalpha(guess):  
        if warnings_left > 0:
            print("Oops! That is not a valid letter. You have", str(warnings_left-1), "warnings left:", end = " ")
        else:
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", end = " ")
        return True
    elif guess.lower() in letters_guessed:
        if warnings_left > 0:
            print("Oops! You've already guessed that letter. You have", str(warnings_left-1), "warnings left:", end = " ")
        else:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", end = " ")
        return True
    else:
        return False

def calculate_unique_letters(secret_word):
    unique_chars = {}
    for char in secret_word:
        unique_chars[char] = 1
    return len(unique_chars)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_left = 6
    warnings_left = 3
    unique_letters = calculate_unique_letters(secret_word)

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", str(len(secret_word)), "letters long.")
    print("You have", str(warnings_left), "warnings left.")
    print("-------------")

    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        print("You have", str(guesses_left), "guesses left")
        print("Available letters:", str(get_available_letters(letters_guessed)))
        guess = input("Please guess a letter: ")
        if check_and_give_warning(guess, letters_guessed, warnings_left):
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print(get_guessed_word(secret_word, letters_guessed))
        else: #proper input and not guessed the letter yet
            letters_guessed.append(guess.lower())
            if(guess in secret_word):
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed)) #you need to fix this because the first e.g. and second e.g. have different formats for the thing ("Oops! That letter is not in my word." vs what u have rn was how it was in the second e.g.)
                if guess.lower() in "aeiou": #vowels
                    guesses_left-=2
                else:
                    guesses_left-=1
        print("-------------")

    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", str(unique_letters*guesses_left))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")

hangman("tact")
