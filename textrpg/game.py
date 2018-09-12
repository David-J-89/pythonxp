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
        self.hp = 0
        self.mp = 0
        self.status_effects = []


myPlayer = player()
