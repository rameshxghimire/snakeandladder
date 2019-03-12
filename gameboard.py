"""
    gameboard.py
    contains board elements such as the grid, snakes' positions and ladders' positions.
"""

# define the snakes and ladder
snakes = {99: "06", 91: "89", 78: "45", 70: "31", 64: "21", 58: "15"}  # snakes bring player down
ladders = {3: "12", 9: "29", 17: "56", 19: "67", 34: "88", 42: "90"}  # ladders take player up


def snake_alert(snakes, user_position):
    """Alerts users about next snakes.

    :param snakes: snakes dictionary
    :type snakes: dict
    :param user_position: players' position attribute
    :type user_position: int
    """

    next_snakes = []
    for key in snakes.keys():
        if key > user_position:
            next_snakes.append(key)
    print(f"SNAKE Alert: \nNext snakes are at: \n{sorted(next_snakes)}")
    print(f"Be careful not to get eaten by them")


def ladder_alert(ladders, user_position):
    """Alerts users of next ladder.

    :param ladders: ladders dictionary
    :type ladders: dict
    :param user_position: players' position attribute
    :type user_position: int
    """

    next_ladders = []
    for key in ladders.keys():
        if key > user_position:
            next_ladders.append(key)
    print(f"LADDERS ahead: \nNext ladders are at: \n{sorted(next_ladders)}")
    print("Try to get to one to climb up")
