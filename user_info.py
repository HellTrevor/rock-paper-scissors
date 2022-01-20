def get_user_item():
    while True:
        user_item = input('Please, write your item (rock, paper, scissors, exit - 0): ')
        user_item = user_item.lower()
        if user_item == '0':
            print('End.')
            return user_item
        elif user_item != 'rock' and user_item != 'scissors' and user_item != 'paper':
            print('Invalid data . . .')
            continue
        return user_item


def get_user_name():
    while True:
        user_name = input('Please, write your name: ')

        if user_name == '':
            print('You cant ignore your name. Please, try again')
            continue
        else:
            return user_name
