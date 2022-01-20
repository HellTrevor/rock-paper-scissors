from user_info import get_user_name, get_user_item
from get_computer_item import get_computer_item
from battle_result import battle_result

user_name = get_user_name()
user_item = get_user_item()

while user_item != '0':

    computer_item = get_computer_item()
    battle_result(user_item, computer_item, user_name)
    user_item = get_user_item()
