"""
Represents a round of the game, storing things like word,
time, skips, drawing player and other stuffs
"""
import time
from _thread import *
from chat import Chat

class Round:
    
    def __init__(self, word, player_drawing, players):
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player: 0 for player in players}
        self.chat = Chat(self)
        self.time = 75
        start_new_thread(self.time_thread, ())
        
    def time_thread(self):
        while self.time > 0:
            time.sleep(1)
            self.time -= 1
        self.__end_round("Time is up")
        
    def guess(self, player, wrd):
        correct = wrd == self.word
        
        if correct:
            self.player_guessed.append(player)
            # TODO implement scoring system here
    
    def player_left(self, player):
        if player in self.player_scores:
            del self.player_scores[player]
            
        if player in self.player_guessed:
            del self.player_guessed[player]
            
        if player == self.player_drawing:
            self.__end_round("Drawing player leaves")
            
    def __end_round(self, msg):
        # TODO implement end round functionality
        pass