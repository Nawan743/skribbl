"""
Stores the state of the drawing board
"""

class Board:
    
    ROWS = COLS = 720
    
    def __init__(self):
        self.__board = self.__crete_empty_board()
    
    @property    
    def board(self):
        return self.__board
        
    def update(self, x, y, color):
        self.__board[y][x] = color
        
    def clear(self):
        self.__board = self.__crete_empty_board()
        
    def update(self, x, y, color):
        pass
    
    def __crete_empty_board(self):
        return [[(255,255,255) for _ in range(self.COLS)] for _ in range(self.ROWS)]