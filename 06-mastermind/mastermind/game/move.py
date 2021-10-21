class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (integer): The number guessed by the user.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess

    def get_pile(self):
        """Returns the guess.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess