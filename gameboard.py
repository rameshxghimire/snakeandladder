"""
    gameboard.py
    contains board elements such as the grid, snakes' positions and ladders' positions.
"""


# imports
import random
import time


# define the snakes and ladder
snakes = {99: "06", 91: "89", 78: "45", 70: "31", 64: "21", 58: "15"}  # snakes bring player down
ladders = {3: "12", 9: "29", 17: "56", 19: "67", 34: "88", 42: "90"}  # ladders take player up


# function for next snake alert
def snake_alert(snakesdict, user_position):
    """Alerts users about next snakes.

    :param snakesdict: snakes dictionary
    :type snakesdict: dict
    :param user_position: players' position attribute
    :type user_position: int
    """

    next_snakes = []
    for key in snakes.keys():
        if key > user_position:
            next_snakes.append(key)
    print(f"SNAKE Alert: \nNext snakes are at: \n{sorted(next_snakes)}")
    print(f"Be careful not to get eaten by them")


# function for next ladder info
def ladder_alert(laddersdict, user_position):
    """Alerts users of next ladder.

    :param laddersdict: ladders dictionary
    :type laddersdict: dict
    :param user_position: players' position attribute
    :type user_position: int
    """

    next_ladders = []
    for key in ladders.keys():
        if key > user_position:
            next_ladders.append(key)
    print(f"LADDERS ahead: \nNext ladders are at: \n{sorted(next_ladders)}")
    print("Try to get to one to climb up")


# ask the number of players
def player_number():
    """
    asks how many players will be playing.

    :return player_num: number of players
    """
    player_num = ""
    while not player_num.isnumeric():
        player_num = input("How many players (Enter a valid number)? ")
    player_num = int(player_num)
    return player_num


# # function to make a player list
def player_list_maker(player_num):
    """
    makes a list of players

    :param player_num: number of players
    :type player_num: int
    :return player_list: list of players
    """
    player_list = []
    for each_one in range(player_num):
        while True:
            player_name = input(f"What is the name of player {each_one + 1}? ")
            if not player_name.isalpha():
                continue
            else:
                player_list.append(player_name.upper())
                break
    return player_list


# dice roll function
def dice_roll():
    """
    mimics dice roll by giving a random number between 1 to 6.

    :return dice_roll_result: int result of the dice roll
    """
    print(f"\033[93m \n__ROLLING THE DICE__\033[00m")
    print(f"\033[93m *-*-*_*-*-*_*_*-*-*_*-*-* \033[00m")
    dice_roll_result = random.randint(1, 7)
    print(f"\033[93m Your number is: \033[00m", end="")
    time.sleep(10)
    print(f"\033[93m {dice_roll_result} \033[00m")
    return dice_roll_result


# set player position to 1 for the start of the game
def set_player_position(player_list):
    """
    sets all players' initial positions to 1 on the game board

    :param player_list: list of players
    :type player_list: list
    :return player_position: dictionary containing players and their position (default 1)
    """
    player_position = {}
    for individual_players in player_list:
        player_position[individual_players] = 1
    return player_position


