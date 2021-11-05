from game.word import Word
from game.buffer import Buffer
from game.score import Score
from game import constants
from game.point import Point

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
        self._score_board = Point(0,1)
        self._word = Word()
        self._input_service = input_service
        self._letter = ""
        self._score = 0
        self._words = ""
        self._buffer = Buffer()

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
        for word in self._words:
            word.move_next()
            if(not word.check_position()):
                # Checking if word has moved off of the screen and needs to be replaced
                self._words.remove(word)
                #Appending words 
                self._words.append(Word())
        if not len(self._buffer.get_chars()) == 0: 
            recent_char = self._buffer.get_chars()[len(self._buffer.get_chars()) - 1]
            if (recent_char == '*'):
                #Reseting the buffer
                self._buffer.reset_buffer()
            else:
                for word in self._words:
                    if (self._buffer.compare(word.get_text())):
                        self._score.add_points(1)
                        self._words.remove(word)
                        self._words.append(Word())
                        continue

        self._input_service.window_should_close()

    def _do_outputs(self):
        pass
                 
        
    def _do_updates(self):
        pass

    def _do_outputs(self):
       pass
