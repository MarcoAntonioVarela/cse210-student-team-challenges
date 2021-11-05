from game import constants
from game.point  import Point
from game.actor import Actor
import random

class Words(Actor):

    """A list of many actors creating a list of words. Facilitates the points for each word (per word?), 
    and the generation of new words.

    """
    
    def __init__(self):
         """The class constructor.
        
        Argumentos:
            self (Words): An instance of Words.
        """
         super().__init__()
         self._words = []
         self._points = 0
         self._prepare_list()
        

    
    def get_all(self):
        """Gets all the words from the list of words the player can try to type. 
        
        Argumentos:
            self (words): instances of words
        returns:
            list of words to be typed
        """
        return self._words
        

    def move_word(self, word, x, y):
        """Moves the word along the predetermined x,y plane
        
        Argumentos:
            self (words): an instance of words
            text (string) the words text.
            x (integer): A horizontal distance.
            y (integer): A vertical distance.
            """
        direction = Point(x, y)
        word = self._words[word]
        word.set_velocity(direction)
        word.move_next()
        
    def word_check(self, word):
        '''Checks the users typed input with the word list. Gets 
        Argumentos:
            self (words): an instance of Words.
            text (string) the words text.
        '''        
        for i in range(0, len(self._words)):
            text = self._words[i]

            if text.get_text() == word:
                self._set_points(word)
                self._words[i].set_text(constants.LIBRARY[random.randint(0, len(constants.LIBRARY))])
                return self._points
            
        return 0


    def _add_word(self, text, position, velocity):
        """
        Adds a new word to the words list using the passed in text, position and velocity.
        Argumentos
            self (Words): an instance of words
            text (string) the words text.
            position (Point): The word's position.
            velocity (Point): The word's velocity.
        """
        word = Actor()
        word.set_text(text)
        word.set_position(position)
        word.set_velocity(velocity)
        self._words.append(word)
        

<<<<<<< HEAD
    def check_position(self):
        if (self.get_position().get_x() + (len(self.get_text()) - 1) > constants.MAX_X):
            return False
        return True

=======
    def _prepare_list(self):
        """Prepares the word list by adding words from the library constant words.txt.
        
        Argumentos
            self (Words): an instance of Words.
        """
        for i in range(constants.STARTING_WORDS):
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2 - 2)
            #The following line will open the Library from our constants file "LIBRARY = open(PATH + "/words.txt").read().splitlines()"
            text = constants.LIBRARY[random.randint(0, len(constants.LIBRARY))]
            position = Point(x, y - i)
            velocity = Point(1, 0)

            self._add_word(text, position, velocity)

    def _set_points(self, word):
        """Sets _points equal to the length of word.
        Argumentos:
            self (Words): an instance of Words.
            word (string): the word to check the length of.
        """
        self._points = len(word)
>>>>>>> b142ed8cbd9ec9061c5ddd57fea60f9b2dafb624
