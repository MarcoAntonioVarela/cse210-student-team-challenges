from time import sleep
from game.word import Word
#from game.buffer import Buffer
from game.score import Score
from game import constants

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
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        #self._score_board = Point()
        self._snake = Word()
        self._input_service = input_service
        self._letter = ""

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")

        while self._keep_playing == True:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close() == True:
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        self._letter = self._input_service.get_letter()
        
    def _do_updates(self):
        pass

    def _do_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._score)
        for word in self._words:
            self._output_service.draw_actor(word)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()