from game.word import Word
from game.buffer import Buffer
from game.score import Score
from game import constants
from game.point import Point
import random

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
       
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._keep_playing = True
        self._input_service = input_service
        self._output_service = output_service
        self._word = Word()
        self._letter = ""
        self._score = 0
        self._scores = Score()
        self._words = [""]
        self._buffers = Buffer()
        self._buffer = ""
        #created word_position, ideally should let the words spawn in random positions along the Y axis
        self.word_position = Point(random.randint(600, 750), random.randint(0, constants.MAX_Y))

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        self._letter = self._input_service.get_letter()
        self._input_service.window_should_close()  
        
    def _do_updates(self):
        self._words = self._word.word_typed(self._score)

        # for self._word in self._words:
        #     self._word.move_next()
        #     if(not self._word.check_position()):
        #         # Checking if word has moved off of the screen and needs to be replaced
        #         self._words.remove(self._word)
        #         #Appending words 
        #         self._words.append(Word())
        if not len(self._letter) == 0: 
            if (self._letter == '*'):
                #Reseting the buffer
                self._buffers.reset()
            else:
                # for self._word in self._words:
                    #if (self._buffers.compare(self._word.get_text())):
                self._buffer = self._buffers.add_letter(self._letter)
                self._score = self._scores.add_points(1)
                        # self._word.remove(self._word)
                        # self._word.append(self._word)
                        # continue

        self._input_service.window_should_close()

    def _do_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_actor(f"Score: {self._score}", constants.SCORE_BOARD)
        # for word in self._words:
        #     #added word position to draw_actor
        self._output_service.draw_actor(self._words, self.word_position)
        self._output_service.draw_actor(f"Buffer: {self._buffer}", constants.BUFFER_POSITION)
        self._output_service.flush_buffer()
        self._input_service.window_should_close()
