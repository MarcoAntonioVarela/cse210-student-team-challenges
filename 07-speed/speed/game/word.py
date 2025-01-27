import random
from game import constants
from game.actor import Actor
from game.point import Point
class Word(Actor):
    """A list of many actors creating a list of words. Facilitates the points for each word (per word?), 
     and the generation of new words.
     """
    def __init__(self):
        """The class Constructor
        """
        super().__init__()
        self._points = 0
        self._typed = False

    def set_word(self, word, point, velocity,score):
        """Sets all of the actor variables to the values needed
        """
        self.set_text(word)
        self.set_position(point)
        self.set_velocity(velocity)
        self._points = score
        self._typed = False
    def get_points(self):
        """Returns points
       
        """
        return self._points
    def word_typed(self, score):
        """Runs when a word is typed, sets text to '-' and _typed to True
        """
        self.set_text(f'+{score}')
        self._typed = True
    
    def get_typed(self):
        """Returns bool, True if the value was typed
        
        """
        return self._typed
# from game import constants
# from game.point  import Point
# from game.actor import Actor
# import random
# class Word(Actor):
#     """A list of many actors creating a list of words. Facilitates the points for each word (per word?), 
#     and the generation of new words.
#     """
    
#     def __init__(self):
#          """The class constructor.
        
#         Argumentos:
#             self (Words): An instance of Words.
#         """
#          super().__init__()
#          self._words = []
#          self._points = 0
#          #self._prepare_list()
#          self.set_position(Point(200, 200))
#          self.set_velocity = constants.MAX_SPEED
         
#     def _choose_word(self):
#         word = random.choice(constants.LIBRARY)
#         return word
#     def get_all(self):
#         """Gets all the words from the list of words the player can try to type. 
        
#         Argumentos:
#             self (words): instances of words
#         returns:
#             list of words to be typed
#         """
#         for i in range(5):
#             word = self._choose_word()
#             self._words.append(word)
#         return self._words
        
#     def move_word(self, word, x, y):
#         """Moves the word along the predetermined x,y plane
        
#         Argumentos:
#             self (words): an instance of words
#             text (string) the words text.
#             x (integer): A horizontal distance.
#             y (integer): A vertical distance.
#             """
#         direction = Point(x, y)
#         word = self._words[word]
#         word.set_velocity(direction)
#         word.move_next()
        
#     def word_check(self, word):
#         '''Checks the users typed input with the word list. Gets 
#         Argumentos:
#             self (words): an instance of Words.
#             text (string) the words text.
#         '''        
#         for i in range(0, len(self._words)):
#             text = self._words[i]
#             if text.get_text() == word:
#                 self._set_points(word)
#                 self._words[i].set_text(constants.LIBRARY[random.randint(0, len(constants.LIBRARY))])
#                 return self._points
            
#         return 0
#     def _add_word(self, text, position, velocity):
#         """
#         Adds a new word to the words list using the passed in text, position and velocity.
#         Argumentos
#             self (Words): an instance of words
#             text (string) the words text.
#             position (Point): The word's position.
#             velocity (Point): The word's velocity.
#         """
#         word = Actor()
#         word.set_text(text)
#         word.set_position(position)
#         word.set_velocity(velocity)
#         self._words.append(word)
        
#     # def _prepare_list(self):
#     #     """Prepares the word list by adding words from the library constant words.txt.
        
#     #     Argumentos
#     #         self (Words): an instance of Words.
#     #     """
#     #     for i in range(constants.STARTING_WORDS):
#     #         x = int(constants.MAX_X / 2)
#     #         y = int(constants.MAX_Y / 2 - 2)
#     #         #The following line will open the Library from our constants file "LIBRARY = open(PATH + "/words.txt").read().splitlines()"
#     #         text = constants.LIBRARY[random.randint(0, len(constants.LIBRARY))]
#     #         position = Point(x, y - i)
#     #         velocity = Point(1, 0)
#     #         self._add_word(text, position, velocity)
#     def _set_points(self, word):
#         """Sets _points equal to the length of word.
#         Argumentos:
#             self (Words): an instance of Words.
#             word (string): the word to check the length of.
#         """
#         self._points = len(word)