import random

class Board:
    """
    The playing surface.
    """
    def _create_list(self):
        ran_num = random(1000,9999)
        code_list = ran_num.split()
        return code_list

    def _create_guess_list(self, guess):
        guess_list = guess.split()
        return guess_list
        