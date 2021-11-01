import random
from game.actor import Actor
from game.point import Point

class Score(Actor):
    """ The responsibiliti of Score is to keep track of the points of the player
    
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        """
        super().__init__()
        self._points = 0
        position = Point(1, 0)
        self.set_position(position)
        self.set_text(f"Score: {self._points}")
    
    def add_points(self, points):
        """This function add the given points to the running total and updates the text.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")