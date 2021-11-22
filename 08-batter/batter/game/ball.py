from game.point import Point
from game.actor import Actor
from game import constants



class Ball(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()
        self._image = constants.IMAGE_BALL
        self._height = constants.BALL_HEIGHT
        self._width = constants.BALL_WIDTH

        point = Point(-7,-1)
        self._velocity = point

        self._position = Point(x_location,y_location)

    def get_position(self):
        return self._position
