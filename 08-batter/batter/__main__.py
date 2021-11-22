from os import X_OK
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.brick import Brick
from game.ball import Ball
from game.move_actors_action import MoveActorsAction
from game.handle_off_screen_action import Handle_Off_Screen_Action
from game.paddle import Paddle
#from game.control_actors_action import C
# TODO: Add imports similar to the following when you create these classes
# from game.brick import Brick
# from game.ball import Ball
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {} 
    #brick1 = Brick(10,10)
    #brick2 = Brick(100,10)
    #brick3 = Brick(200,10)
    cast["bricks"] = []
     
    for y in range(5):
        
        for x in range(13):
            brick = Brick((x*61) ,(y*45))
            cast["bricks"].append(brick)

    #print(brick1.get_position().get_x(),brick1.get_position().get_y())
    #print(brick2.get_position().get_x(),brick1.get_position().get_y())
    #print(brick3.get_position().get_x(),brick1.get_position().get_y())
    
    # TODO: Create bricks here and add them to the list

    cast["balls"] = []

    ball = Ball(355,500)
    cast["balls"].append(ball)

    # TODO: Create a ball here and add it to the list

    cast["paddle"] = []

    paddle = Paddle(350,560)
    cast["paddle"].append(paddle)
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    
    #control_actors_action = ControlActorsAction(input_service)
    draw_actors_action = DrawActorsAction(output_service)
    handle_off_screen_action = Handle_Off_Screen_Action()

    # TODO: Create additional actions here and add them to the script

    script["input"] = []
    script["update"] = [move_actors_action,handle_off_screen_action]
    
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
