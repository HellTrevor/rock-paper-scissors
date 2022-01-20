import random


def get_computer_item():
    possible_items = ["rock", "paper", "scissors"]
    computer_item = random.choice(possible_items)
    print('AI item: ', computer_item)
    return computer_item
