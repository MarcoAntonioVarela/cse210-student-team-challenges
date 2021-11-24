from typing import cast
from game.action import Action
from game.actor import Actor
from game.point import Point


class MoveActorsAction(Action):

    def execute(self,cast):

        velocity = cast['balls'][0].get_velocity()
        position = cast['balls'][0].get_position()

        #Merging/separating both x and y values so we can use them in our Point parameters
        new_x_position = velocity.get_x() + position.get_x() 
        new_y_position = velocity.get_y() + position.get_y() 


        new_position = Point(new_x_position,new_y_position)

        cast["balls"][0].set_position(new_position)
        
        ######################################################
        
        velocity = cast['paddle'][0].get_velocity()
        position = cast['paddle'][0].get_position()

        new_x_position = velocity.get_x() + position.get_x() 

        #The paddle does not need the y position because we are only moving it left to right
        #new_y_position = velocity.get_y() + position.get_y() 


        new_position = Point(new_x_position,position.get_y())

        cast["paddle"][0].set_position(new_position)
