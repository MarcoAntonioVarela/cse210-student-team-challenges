#Week 06 team activity
#10/22/2022


import random

class Mastermind:
    """This is the designated playing "surface".
    Stereotype:
    Information holder
    Service Provider
    Attributes:
        _code_list - list of numbers"""

    def __init__(self):
        """Constructor
        Args:
            self - an instance of mastermind"""

        # initialize variables
        self._code_list = []
        self._prepare()
    
    def _prepare(self):
        """Generate the secret code and turn it into a list
        Args
            self - an instance of mastermind"""
        code = str(random.randint(1000, 9999))
        self._code_list = [str(x) for x in str(code)]

    def compare(self, guess_list):
        """Responsible for comparing the guess and code and returning the hint value(list)
        Args
            self - an instance of mastermind
            guess_list - a list with str contained guess
        Returns
            hint_value - a list with str contained hint"""
        guess = guess_list
        code = self._code_list
        hint = ["*","*","*","*"]

        for i, number in enumerate(guess):
            if code[i] == number:
                hint[i] = "x"
            elif number in code:
                hint[i] = "o"
            else:
                hint[i] = "*"
        return hint
        
    def hint(self, players):
        """Using compare return a str output with player guesses and hints
		Args
            players -  a list of player objects that will be passed in from director,
            here for the get_name and get_move functions
        Returns
            output - a str with players, their guesses, and applicable hints"""
        
        output = "\n--------------------\n"
        for player in players:
            hint = ""
            guess = ""
            name = player.get_name()
            turn = player.get_turn()
            guess_list = turn.get_turn()
            hint_list = self.compare(guess_list)

            for item in guess_list:
                guess += str(item)
            for symbol in hint_list:
                hint += symbol 

            output += (f'Player {name}: ' + f'{guess}, ' + f'{hint}\n')
        output += "--------------------\n"
         
        return output


    def is_won(self, guess_list):
        """Responsible for seeing if the guess matches the code, if so return boolean True, 
        otherwise False
        Args
            self - an instance of mastermind
        Returns 
            bool - True if guess_list matches _code_list, otherwise False"""
        
        if guess_list == self._code_list:
            return True
        else:
            return False