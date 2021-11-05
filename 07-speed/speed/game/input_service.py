#Updating code following Brother Burton's provided template

import sys
import raylibpy
class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).
    Stereotype: 
        Service Provider
    Attributes:
        _screen (Screen): An Asciimatics screen.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self.letter = ""
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.
        Args:
            self (InputService): An instance of InputService.
        Returns:
            string: The letter that was typed.
        """
        event = raylibpy.get_key_pressed()
        if not event is None:
            if event == 27:
                sys.exit()
            elif event == 10: 
                self.letter = "*"
            elif event >= 97 and event <= 122: 
                self.letter = chr(event)
        return self.letter

    def window_should_close(self):
        event = raylibpy.is_key_down(raylibpy.KEY_ESCAPE)
        if event == True:
            return True
        else:
            return False