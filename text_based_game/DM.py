"""DM.py our Dungeon Master for the game.

Will handle all the tasks and functions of a Dungeon Master.
"""
# Algor 1 - basic - generaterandom number between 6 and 18
# return random.randint(6, 18)

# Algor 2 (your choice) TODO:


import random

def roll_stats() -> int:
    """Gets stats for a characters attributes"""
    return random.randint(6, 18)

def get_modifier(stats) -> int:
    modifier = 0
    if stats == 6 or 7():
        modifier = -2
    if stats == 8 or 9():
        modifier = -1
    if stats == 10 or 11():
        modifier = 0
    if stats == 12 or 13():
        modifier = +1
    if stats == 14 or 15():
        modifier = +2
    if stats == 16 or 17():
        modifier = +3
    if stats == 18():
        modifier = +4
    return stats + modifier

if __name__ == "__main__":
    print("I am the DM here")