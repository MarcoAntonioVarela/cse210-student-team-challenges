from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """Points earned. The responsibility of Buffer is to keep track of the players letters.
   
    """
    def __init__(self):
        """The class construction for buffer.  initializes word set to blank, the position and updates the text
        Argumentos:
            self is an instance of Buffer
        """

        super().__init__()
        self._word = ""
        self.chars = ""
    
    def add_letter(self, letter):
        """Adds the give letter to the buffer and sets the buffer text with the word and letter.
        
        """
        self._word += letter
        return self._word

        
    def get_word(self):
        """Gets the word(s)
        """
        #Please test this again, I am not sure if this will return the word
        return self._word

    def reset(self):
        """I think this will reset the word to an empty string when called.

        """
        self._word = ""

    def get_chars(self):
        return self.chars