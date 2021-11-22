from game.paddle import Paddle
from game.point import Point
from game.actor import Actor
from game import constants


class ControlActorsAction(Actor):

    def __init__(self, input_service):

        self._input_service = input_service
        

    def excecute(self,cast):

        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] 
        paddle.set_velocity(direction.scale(constants.PADDLE_SPEED)) 

        