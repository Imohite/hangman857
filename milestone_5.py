import random

word_list = ['apples', 'oranges', 'grapes', 'bananas', 'kiwis']
print(word_list)

class Hangman():
    ''' This class is used to create Hangman, 
    a classic game in which a player thinks of a word and 
    the other player tries to guess that word within a certain amount of attempts.
    This is an implementation of the Hangman game, 
    where the computer thinks of a word and the user tries to guess it.

    Attributes:
    word_list (list): list of words
    word (str): The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
    word_guessed (list): list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet
    num_lives (int): The number of lives the player has at the start of the game. Default value set to 5.
    list_of_guesses (list): list of the guesses that have already been tried. Set this to an empty list initially.
    '''

    def __init__(self, word_list, num_lives=5):
        ''' 
         See help(Hangman) for more information

        This method is a class constructor

        Attributes:
            see help(Hangman)
        '''

        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(self.word_list)

        self.word_guessed = []

        for i in range(0,len(self.word)):
            self.word_guessed.append('_')

        print(self.word_guessed)

        self.num_letters = len(set(self.word))
        print('Number of unique letter is the word', self.num_letters)
        
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        '''
        Checks if the guessed letter is in the word.

        Attributes:
        guess (str) : guessed letter input by the user.

        Returns: nothing returned, but adjusts num_lives and num_letters.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    print('Status: ', self.word_guessed)
            self.num_letters -=1
        else:
            print(f'Sorry, {guess} is not in the word')
            self.num_lives -=1
            print(f'You have {self.num_lives} lives left')
    

    def ask_for_input(self):
        ''' 
        Requests the user to enter a letter and verifies if single alphabetical character is entered and if it has not been entered previously.
        Call check_guess method.

        Attributes:
        guess (str) : guessed letter input by the user.

        Returns: nothing returned.
        '''
        while True:
            guess = input('Enter a single alphabetical character: ')
            len_guess = len(guess)
            if not(guess.isalpha() == True and len_guess == 1):
                print('Invalid letter. Please enter a single alphabetical character again: ')
            elif guess in self.list_of_guesses :
                print('You have already tried that letter')
                print('Your previous guesses include: ', self.list_of_guesses)
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    num_lives = 3
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0 :
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


play_game(word_list)

