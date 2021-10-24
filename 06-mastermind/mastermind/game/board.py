import random

class Board:
    """
    Displays the playing surface
    Attributes:
        guess: player's guess
        code: secret code trying to be guessed
        player: who is playing        
    """
    def __init__(self):
        """
        The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guess = 0
        self.random_num = random.randint(1000,9999)
        self.player = None

    def _create_list(self):
        """
        Turns the code into a list

        Args:
            self (Director): an instance of Director.
        """
        code_list = self.random_num.split()
        return code_list

    def _create_guess_list(self):
        """
        Turns the guess into a list

        Args:
            self (Director): an instance of Director.
        """
        guess_list = list(str(self.guess))
        return guess_list
        
    def _create_border(self):
        """
        Creates the border for the game display

        Args:
            self (Director): an instance of Director.
        """
        return f"--------------------"

    def _display_player(self, guess_accuracy):
        """
        Displays the player and how accurate their guess is

        Args:
            self (Director): an instance of Director.
            guess_accuracy: The hints given after the player makes a guess
        """
        return f"Player {self.player}: {self.guess}, {guess_accuracy}"