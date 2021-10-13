import os
from game.parachute_tracker import Parachute_Tracker

class Console:
    """A code template for a computer console. The responsibility of this
    class of objects is to control CLI display. This includes clearing the
    screen, coordinating the printing of game screen instances (with the
    parachute, word letters/blanks, and prompt), and receiving user input.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        director (Director): An instance of the class of objects known as Director.
        guess (string): A one-character string of promted user input.
        parachute_tracker (Parachute_Tracker): An instance of the class of objects known as Parachute_Tracker.
    """


    def __init__(self):
        """The class constructor.

        Args:
            self (Console): an instance of Console.
            Parachute_Tracker (Console): an instance of Parachute_Tracker.
        """
        self.guess = ""
        self.Parachute_Tracker = Parachute_Tracker()

    def clear_screen(self):
        """Detects OS type and sends appropriate console command to clear screen.

        Args:
            self (Console): An instance of Console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def write(self, word_progress = str, num_strikes = int):
        """Performs all output to console, prompts user input.

        Args:
            self (Console): An instance of Console.
        """
        prompt = "\nGuess a letter [a-z]: "
        while True:
            self.clear_screen()

            print("\n" + word_progress)

            print(self.Parachute_Tracker.get_parachute(num_strikes))

            letter = input(prompt).lower().strip()
            if letter.isalpha() and len(letter) == 1 and (letter not in word_progress):
                break

            prompt = "\nPlease enter a letter [a-z]\nyou have not guessed yet: "

        self.guess = letter

    def read(self):
        """Returns user's letter guess as one-character string.

        Args:
            self (Console): An instance of Console.
        """
        # (AH)
        # return input(msg)
        return self.guess

    def print_loss(self, word = str):
        self.clear_screen()
        print("\n\n\tYou lost. Better luck next time.")
        print(f"\n\tThe word was '{word}'.")
        input("\n\tPress ENTER to exit.")
        self.clear_screen()

    def print_victory(self, word = str):
        self.clear_screen()
        print("\n\n\tYou won! Well done!")
        print(f"\n\tThe word was '{word}'!")
        input("\n\tPress ENTER to exit.")
        self.clear_screen()