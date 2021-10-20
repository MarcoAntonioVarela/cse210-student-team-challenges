class Player:
    def __init__ (self, name):
        self._name = name
        self._move = None

    def get_name(self):
        return self._name
    
    def get_move(self):
        return self._move

    def set_move(self, move):
        self._move = move