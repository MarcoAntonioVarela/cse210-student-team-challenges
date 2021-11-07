#I updated this code by following Brother Burton's template

#Importing the OS module
#What is the OS module? it is a built-in module (We don't need to install any third-party libraries)
#The OS module in Python provides functions for interacting with the operating system.
#OS is normally use to make,move,rename and remove directories.

import os
from game.point import Point
#os.environ['RAYLIB_BIN_PATH'] = '.'
MAX_X = 800
MAX_Y = 400
FRAME_RATE = 30

DEFAULT_SQUARE_LENGTH = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 5

MAX_SPEED = 5
WORD_GENERATION_RATE = 0.02

BUFFER_POSITION = Point(1, MAX_Y - 30)
SCORE_BOARD = Point(1, MAX_Y - 390)

STARTING_WORDS = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()