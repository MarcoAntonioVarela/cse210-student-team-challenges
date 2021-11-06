import random
from game.actor import Actor
from game.point import Point

class Score(Actor):
    """ The responsibiliti of Score is to keep track of the points of the player
    
    """
    def __init__(self):
        """The class constructor. Calls the superclass constructor, initializes points to zero, sets the position and updates the text.
        """
        super().__init__()
        self._points = 0
        position = Point(1, 0)
        self.set_position(position)
        #self.text = f"Score: {self._points}"
        self._points = 0
    
    def add_points(self, points):
        """This function add the given points to the running total and updates the text.
        """
        self._points += points
        return self._points
        #We need to verify if it is succesfully displaying the following message
        # self.set_text = f"Score: {self._points}"
        # return self.set_text