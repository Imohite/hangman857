import random

word_list = ['apples', 'oranges', 'grapes', 'bananas', 'kiwis']
print (word_list)



class Hangman():

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(self.word_list)
        print(self.word)

        self.word_guessed = []

        for i in range(0,len(self.word)):
            self.word_guessed.append('_')

        print(self.word_guessed)

        self.num_letters = len(set(self.word))
        print('Number of unique letter is the word', self.num_letters)

        
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -=1
        else:
            print(f'Sorry, {guess} is not in the word')
            self.num_lives -=1
            print(f'You have {self.num_lives} lives left')
    

    def ask_for_input(self):
        while True:
            guess = input('Enter a single alphabetical character: ')
            len_guess = len(guess)
            print(guess)
            if not(guess.isalpha() == True and len_guess == 1):
                print('Invalid letter. Please enter a single alphabetical character again: ')
            elif guess in self.list_of_guesses :
                print('You have already tried that letter')
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


hangman = Hangman(word_list)
hangman.ask_for_input()




'''class Hangman - attributes
word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
num_lives: int - The number of lives the player has at the start of the game. Default value set to 5.
word_list: list - A list of words
list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially
'''





    

        
