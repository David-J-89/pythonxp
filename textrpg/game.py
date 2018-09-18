# Python Text RPG
# davidj

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####


class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
        self.game_over = False


myPlayer = player()

##### Title Screen #####


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()  # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ('play', 'help', 'quit'):
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()  # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('~~~~~~~~~- Play -~~~~~~~~~~~')
    print('~~~~~~~~~- Help -~~~~~~~~~~~')
    print('~~~~~~~~~- Quit -~~~~~~~~~~~')
    print('   Copyright 2018 davidj    ')
    title_screen_selections()


def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    title_screen_selections()

##### GAME FUNCTIONALITY #####


def start_game():

    ##### MAP #####
"""
a1 a2... # PLAYER STARTS AT b2
-------------
|  |  |  |  | a4
-------------
|  |  |  |  | b4...
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_place = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zone_map = {
    'a1': {
        ZONENAME: "TOWN A1",
        DESCRIPTION = ''
        EXAMINATION = 'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b1'
        LEFT = ''
        RIGHT = 'a2'
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION = 'the entrance to the town'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b2'
        LEFT = 'a1'
        RIGHT = 'a3'
    },
    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION = 'the central meeting place of the town'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b3'
        LEFT = 'a2'
        RIGHT = 'a4'
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION = 'government offices in here'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b4'
        LEFT = 'a3'
        RIGHT = ''
    },
    'b1': {
        ZONENAME: "town",
        DESCRIPTION = 'the entrance to the town'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a1'
        DOWN = 'c1'
        LEFT = ''
        RIGHT = 'b2'
    },
    'b2': {
        ZONENAME: "Home",
        DESCRIPTION = 'This is your home!'
        EXAMINATION = 'Your home looks the same - nothing has changed.'
        SOLVED = False
        UP = 'a2'
        DOWN = 'c2'
        LEFT = 'b1'
        RIGHT = 'b3'
    },
    # 'b3': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'b4': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'c1': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'c2': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'c3': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'c4': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'd1': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'd2': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'd3': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },
    # 'd4': {
    #     ZONENAME: "",
    #     EXAMINATION = 'examine'
    #     SOLVED = False
    #     UP = 'up', 'north'
    #     DOWN = 'down', 'south'
    #     LEFT = 'left', 'west'
    #     RIGHT = 'right', 'east'
    # },

}

##### GAME INTERACTIVITY #####


def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print("\n" + "===========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown actions, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())


def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['east', 'right']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.loction = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print("You can trigger a puzzle here.")


##### GAME FUNCTIONALITY #####
def start_game():
    return


def main_game_loop():
    while myPlayer.game_over is False:
    prompt()
    # here handle if puzzles have been solved, boss defaeated, explored, everything, etc.


def setup_game():
    os.system('clear')

    # Name collecting
    question1 = "Hello, what's your name?\n"
    for character in question 1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "Hello, what role do you want to play?\n"
    for character in question 2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ")
    myPlayer.name = player_job
    valid_job = ['warrior', 'mage', 'priest']


title_screen()
