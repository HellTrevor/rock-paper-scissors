import random

user_name = input('Please, write your name: ')
possible_items = ["rock", "paper", "scissors"]
index = 1

while index > 0:

    user_item = input('Please, write your item (rock, paper, scissors, exit - 0): ')
    user_item = user_item.lower()
    computer_item = random.choice(possible_items)

    if user_item == '0':
        print('End.')
        break
    elif user_item != 'rock' and user_item != 'scissors' and user_item != 'paper':
        print('Invalid data . . .')
        continue

    print('AI item: ', computer_item)

    if user_item == 'rock' and computer_item == 'paper':
        print('AI-player win!')
    elif user_item == 'paper' and computer_item == 'scissors':
        print('AI-player win!')
    elif user_item == 'scissors' and computer_item == 'rock':
        print('AI-player win!')
    elif user_item == 'paper' and computer_item == 'rock':
        print(user_name, ' win!')
    elif user_item == 'rock' and computer_item == 'scissors':
        print(user_name, ' win!')
    elif user_item == 'scissors' and computer_item == 'paper':
        print(user_name, ' win!')
    elif user_item == computer_item:
        print('Draw.')
