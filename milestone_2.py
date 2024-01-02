import random

word_list = ['apples', 'oranges', 'grapes', 'bananas', 'kiwis']
print (word_list)

word = random.choice(word_list)
print(word)

loop_flag = 0
while loop_flag == 0:
    guess = input('enter a single letter: ')
    len_guess = len(guess)
    print(guess)
    if len_guess == 1:
        print('single letter entered, valid input')
        loop_flag = 1
    else: 
        print('single letter not entered, invalid input, enter a single letter again')
        loop_flag = 0



