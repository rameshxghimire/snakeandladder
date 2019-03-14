"""
    gameboard.py
    contains board elements such as the grid, snakes' positions and ladders' positions.
"""


# imports
import random
import time


# define the snakes and ladder
snakes = {99: "06", 91: "89", 78: "45", 70: "31", 64: "21", 58: "15", 46: "8", 22: "13"}  # bring plr down
ladders = {3: "12", 9: "29", 17: "56", 19: "67", 34: "88", 42: "90", 56: "90"}  # take player up


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


# player turn rotate function
def player_turn_rotator(player_list):
    """
    takes the player list, rotates in every run to assign current player

    :param player_list: list of all players, list
    :return: rotated player_list, list
    """
    if len(player_list) == 1:
        print(f"\033[93m------------------------------\033[00m")
        print(f"\033[93m{player_list[0]} WINS.\CONGRATULATIONS!\033[00m")
        print(f"\033[93m------------------------------\033[00m")
    else:
        player_name = player_list[0]
        print(f"\033[93m\nIt's {player_list[0]}'s turn\033[00m")
        # copy the current player to the end of the list
        player_list.append(player_list[0])
        # remove the current player from the first position
        player_list.remove(player_list[0])
    return player_list


# extract player name from the rotated player_list, must go always after the player_turn_rotator function
def extract_current_player(player_list):
    """
    extracts current player from the rotated player_list where the current player is moved to -1 position

    :param player_list: list of players, rotated
    :return: player_name, str
    """
    player_name = player_list[-1]
    return player_name


# set player position to 1 for the start of the game
def set_player_position(player_list):
    """
    sets all players' initial positions to 1 on the game board

    :param player_list: list of players
    :type player_list: list
    :return player_position: dictionary containing players & their position (default 0, out of the board)
    """
    player_position = {}
    for individual_players in player_list:
        player_position[individual_players] = 0
    return player_position


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


# change the player position based on the dice roll result
def alter_player_position(player_name, dice_roll_result, player_position, snakes, ladders):
    """
    moves player up on the grid based on the dice roll result number.

    :param player_name: current player, any key of player_position dict.
    :type player_name: Str
    :param dice_roll_result: the result from the dice roll
    :type dice_roll_result: int
    :param player_position: player_position dict
    :type player_position: dict
    :return player_position: dict with new value of the position.
    """
    player_position[player_name] = player_position[player_name] + dice_roll_result
    print(f"Your new position is: {player_position[player_name]}")
    time.sleep(1)
    print(f"\033[93m Checking for Snakes and Ladders: \033[00m", end="")
    time.sleep(2)
    if player_position[player_name] in snakes.keys():
        # set a new position via snakes
        player_position[player_name] = snakes[player_position[player_name]]
        print(f"\033[93mOH NO, You stepped in a Snake. \033[00m")
        print(f"The snake ate you and pooped you out at: {player_position[player_name]}")
        print(f"\033[93mYOUR NEW POSITION IS: {player_position[player_name]} \033[00m")
    elif player_position[player_name] in ladders.keys():
        # set a new position via ladders
        player_position[player_name] = ladders[player_position[player_name]]
        print(f"\033[93mOH NO, You found a ladder. \033[00m")
        print(f"The ladder took you to: {player_position[player_name]}")
        print(f"\033[93mYOUR NEW POSITION IS: {player_position[player_name]} \033[00m")
    else:
        print(f"\033[93mNo Snakes, No ladders. \033[00m")
    return player_position


# set winning condition and logic
def winning_condition(player_position, player_name):
    """
    defines winning logic, selects the winner and removes from the dict

    :param player_position: dictionary with players and their positions
    :type player_position: dict
    :param player_name: current player name
    :type player_name: str
    :return player_position: modified player_position dict if applicable
    """
    if player_position[player_name] == 100:
        print(f"\033[93m*_*_*_*_*_*_*_*_*_*\033[00m")
        print(f"\033[93mCONGRATULATIONS, {player_name} WINS! \033[00m")
        print(f"\033[93m------------------------------\033[00m")
        # removing the winner from the players dict
        del player_position[player_name]
    return player_position

