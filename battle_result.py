def battle_result(user_item, computer_item, user_name):
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
