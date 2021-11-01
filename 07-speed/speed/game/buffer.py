from game import constants
from game.actor import Actor

class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self.chars = ''
        self._position._y = constants.MAX_Y - 1

    def add_char(self, char):
        self.chars += char
        self.set_text(f'Buffer:{self.chars}')

    def get_chars(self):
        return self.chars

    def compare(self, string):
        if (string in self.chars):
            return True
        else:
            return False

    def reset_buffer(self):
        self.chars = ''
        self.set_text(f'Buffer:{self.chars}')