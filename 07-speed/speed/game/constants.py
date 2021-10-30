import os

MAX_X = 600
MAX_Y = 400
FRAME_LENGTH = 0.08
STARTING_WORDS = 5
DIFFICULTY = 1
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
