"""
Represents a player object on the server side
"""

class Player:
    def __init__(self, ip, name):
        self.__ip = ip
        self.__name = name
        self.score = 0
        
    @property
    def score(self):
        return self.score
    
    @property
    def ip(self):
        return self.__ip
    
    @property
    def name(self):
        return self.__name
    
    @score.setter
    def score(self, x):
        self.score += x