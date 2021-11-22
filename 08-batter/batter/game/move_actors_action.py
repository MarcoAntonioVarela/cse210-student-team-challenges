from typing import cast
from game.actor import Actor
from game.point import Point


class MoveActorsAction(Actor):

    def execute(self,cast):

        velocity = cast['balls'][0].get_velocity()
        position = cast['balls'][0].get_position()

        #Merging/separating both x and y values so we can use them in our Point parameters
        new_x_position = velocity.get_x() + position.get_x() 
        new_y_position = velocity.get_y() + position.get_y() 


        new_position = Point(new_x_position,new_y_position)

        cast["balls"][0].set_position(new_position)
