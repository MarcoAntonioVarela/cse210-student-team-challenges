from game.ball import Ball
from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.audio_service import AudioService
from game import constants
class HandleCollisionsAction(Action):

    def execute(self,cast):
        
        physics = PhysicsService()
        collission_ball= cast["balls"][0]
        collission_paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        sound = AudioService()
    
        collission = physics.is_collision(collission_ball,collission_paddle)
        # collission_paddle = PhysicsService.is_collision(collission_paddle,collission_ball)

        if collission == True:
            ball_velocity = collission_ball.get_velocity()
            sound.play_sound(constants.SOUND_BOUNCE)
            dy =ball_velocity.get_y()
            dy *= -1 
            new_velocity = Point(ball_velocity.get_x(),dy)
            collission_ball.set_velocity(new_velocity)
 
        for brick in bricks:
            collided = physics.is_collision(collission_ball,brick)

            if collided == True:
                sound.play_sound(constants.SOUND_BOUNCE)
                ball_velocity = collission_ball.get_velocity()
                dy =ball_velocity.get_y()
                dy *= -1 
                new_velocity = Point(ball_velocity.get_x(),dy)
                collission_ball.set_velocity(new_velocity)
                

                cast["bricks"].remove(brick)

