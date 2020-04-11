import numpy as np

class gameState:
    def __init__(self):
        self.boardSize = 3
        self.ai = [False,False]
        self.Gui = False
        self.board = self.initBoard()
        
    def initBoard(self):
        