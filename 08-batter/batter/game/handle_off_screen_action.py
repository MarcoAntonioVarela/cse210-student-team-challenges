from game.point import Point
from game.constants import MAX_X
from game.action import Action
from game import constants


class Handle_Off_Screen_Action(Action):
    
    def execute(self,cast):
        
        bouncing_balls = cast['balls']

        for ball in bouncing_balls:

            ball_point = ball.get_position()
            x = ball_point.get_x()
            y = ball_point.get_y()
            ball_velocity = ball.get_velocity()
            if x <= 0 or x >= 780:
                
                dx =ball_velocity.get_x()
                dx *= -1 
                #ball_velocity.set_x(dx)
                new_velocity =Point(dx,ball_velocity.get_y())
                ball.set_velocity(new_velocity)
            
            if y <= 0:
                dy =ball_velocity.get_y()
                dy *= -1 
                new_velocity =Point(ball_velocity.get_x(),dy)
                ball.set_velocity(new_velocity)
            





