#This has been updated 10/22/2022

class Roster:
    """A collection of players. The responsibility of Roster is to keep track of the players.
    
    Stereotype: 
        Information Holder
    Attributes:
        _current (integer): The index of the current player.
        _players (list): A list of Player objects.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Roster): an instance of Roster.
        """
        self.current = -1
        self.players = []
        
    def add_player(self, player):
        """Adds the given player to the roster
        
        Args:
            self (Roster): An instance of Roster.
            player (Player): The player object to add.
        """
        if player not in self.players:
            self.players.append(player)

    def get_current(self):
        """Gets the current player object.
        
        Args:
            self (Roster): An instance of Roster.
        
        Returns:
            Player: The current player.
        """
        return self.players[self.current]
    
    def next_player(self):
        """Advances the turn to the next player.
        
        Args:
            self (Roster): An instance of Roster.
        """
        self.current = (self.current + 1) % len(self.players)

    def get_players(self):
        """Returns the list of player objects
        Args:
            self - an instance of roster"""
        return self.players