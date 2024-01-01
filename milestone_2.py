import random


word_list = ['apples', 'oranges', 'grapes', 'bananas', 'kiwis']

print (word_list)

word = random.choice(word_list)

print(word)





x = 0
while x == 0:
    guess = input('enter a single letter: ')
    len_guess = len(guess)
    print(guess)
    if len_guess == 1:
        print('single letter entered, valid input')
        x = 1
    else: 
        print('single letter not entered, invalid input, enter a single letter again')
        x = 0



