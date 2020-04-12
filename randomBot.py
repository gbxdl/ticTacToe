import random

class randomBot():
    def __init__(self,gameState):
        None

    def makeMove(self,gameState):
        return random.choice(list(gameState.possibleMoves()))