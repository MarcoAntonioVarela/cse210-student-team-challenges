from game import constants
from game.point  import Point
from game.actor import Actor
import random

class Word(Actor):
    def __init__(self):
        super().__init__()
        self.set_text(constants.LIBRARY[random.randint(0, len(constants.LIBRARY) - 1)])
        self.set_position(Point(0, random.randint(constants.MAX_Y / 4, constants.MAX_Y - 4))) 
        self.set_velocity(Point(random.randint(1, 3), 0))

    def move_next(self):
        self.set_position(self.get_position().add(self.get_velocity()))
        

    def check_position(self):
        if (self.get_position().get_x() + (len(self.get_text()) - 1) > constants.MAX_X):
            return False
        return True
