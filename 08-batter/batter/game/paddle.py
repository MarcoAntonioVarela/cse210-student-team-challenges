from game.actor import Actor
from game import constants
from game.point import Point 

class Paddle(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()

        self._image = constants.IMAGE_PADDLE
        self._height = constants.PADDLE_HEIGHT
        self._width = constants.PADDLE_WIDTH

        point = Point(-10,-2)
        self._velocity = point

        self._position = Point(x_location,y_location)

    def get_position(self):
        return self._position

