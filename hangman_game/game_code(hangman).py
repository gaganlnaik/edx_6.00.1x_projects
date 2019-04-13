# Hangman game
#

# -----------------------------------


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret=list(secretWord)
    for k in secret:
        if k in lettersGuessed:
            continue
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secret=list(secretWord)
    out=[]
    for i in range(len(secret)):
        if secret[i] in lettersGuessed:
            out.append(secret[i])
        else:
            out.append(' _ ')
    output=''.join(out)
    return output
            

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    guessed=list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in guessed:
            guessed.remove(i)
        else:
            continue
    guess=''.join(guessed)
    return guess
    
   

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    s=list(secretWord)
    print('Welcome to the game, Hangman!')
    print('I am thinking fo a word that is',len(secretWord),'letters long.')
    k=8
    lettersGuessed=[]
    while k>0:
        print('_ _ _ _ _ _ _ _')
        print('You have',k,'guesses left.')
        y=getAvailableLetters(lettersGuessed)
        print('Available letters:',y)
        x=input('Please guess a letter:')
        x=x.lower()
        lettersGuessed.append(x)
        if lettersGuessed[-1] in s and lettersGuessed[-1] in y:
            print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
            if '_' not in getGuessedWord(secretWord, lettersGuessed):
                print('_ _ _ _ _ _ _ _')
                return 'Congratulations, you won!'
        elif x not in y:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
            k-=1
    if k==0: 
           print('_ _ _ _ _ _ _ _')  
           print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
