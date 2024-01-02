import random

word_list = ['apples', 'oranges', 'grapes', 'bananas', 'kiwis']
print (word_list)

random_word = random.choice(word_list)
print(random_word)

def ask_for_input():
    while True:
        guess = input('Enter a single alphabetical character: ')
        len_guess = len(guess)
        print(guess)
        if guess.isalpha() == True and len_guess == 1:
            print('Single letter entered, valid input.')
            break
        else: 
            print('Invalid letter. Please enter a single alphabetical character again: ')
    check_guess(guess)


def check_guess(guess):
    guess = guess.lower()
    if guess in random_word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word')


ask_for_input()


    

        
