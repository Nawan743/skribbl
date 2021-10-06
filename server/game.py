"""
Handles operations related to game and connections
between player, board, chat and round
"""

from round import Round
from player import Player
from board import Board

class Game:
    
    def __init__(self, id, players, thread):
        self.id = id
        self.players = players
        self.words_used = []
        self.connected_thread = thread
        self.board = Board()
        self.player_draw_ind = 0
        self.start_new_round()
        
    def start_new_round(self):
        self.round = Round(self.generate_word, self.players[self.player_draw_ind], self.players)
        if  len(self.players) > self.player_draw_ind:
            self.player_draw_ind += 1  
        else:
            self.player_draw_ind = 0
            self.board.clear()
            self.start_new_round()
            self.end_game()
        
    def player_guess(self, player, guess):
        return self.round.guess(player, guess) 
    
    def player_disconnected(self, player):
        if player in self.players:
            del self.players[player]
        else:
            raise Exception("The player is no longer on the player list!")
    
    def skip(self):
        if self.round:
            new_round = self.round.skips()
            if new_round:
                self.start_new_round()
        else:
            raise Exception("No round started yet!")
    
    def update_scores(self):
        pass
    
    def update_board(self, x, y, color):
        if not self.board:
            raise Exception("No board created!")
        self.board.update(x, y, color)
    
    def end_game(self):
        pass
    
    def generate_word(self):
        # TODO generate a pseudo-word of a list from somewhere
        pass