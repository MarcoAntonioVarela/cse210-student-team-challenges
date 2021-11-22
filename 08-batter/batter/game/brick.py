from game.actor import Actor
from game.point import Point
from game import constants

class Brick(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()
        self._image = constants.IMAGE_BRICK
        self._height = constants.BRICK_WIDTH
        self._width = constants.BRICK_HEIGHT


        self._position = Point(x_location,y_location) 

    def get_position(self):
        return self._position
    
        
    
    

