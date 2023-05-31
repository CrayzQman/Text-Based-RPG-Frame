"""Our character class and their variables

We're going to add a random algorithm for generating stats:
4d6, drop the lowest number, add the rest

Stragey #1
SET 4 varibles each to a random number between 1-6
COMPARE all 4 varibles to see whihc is the least

Stragey #2
SET an empty list (to add each d6 roll)
Repeat 4 times:
    add a random number between  1-6 to the list 
SORT the list from high to low
Remove the lowest number
"""

import random 
import DM

class Character:
    # contructor
    def __init__(self, name):
        self.name = name
        self.strength = DM.roll_stats()
        self.dexterity = DM.roll_stats()
        self.constitution = DM.roll_stats()
        self.attack_modifier = DM.get_modifier(self.strength)


    # methods
    # when printing the character
    def __str__(self) -> str:
        repr = "Character Details:\n"
        repr += f"Name: {self.name}\nStrength: {self.strength}\n"
        repr += f"Dexterity: {self.dexterity}\n"
        repr += f"ATKM: {self.attack_modifier}\n"
        return repr