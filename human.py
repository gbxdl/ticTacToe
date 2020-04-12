import math

class human:
    def __init__(self):
        pass
        
    def makeMove(self,gs,event,fromEdge, width):
        klik=[event.x, event.y]
        row = round( (klik[1] - 1.5*fromEdge) / width)
        col = round( (klik[0] - 1.5*fromEdge) / width)
        
        if 0 <= col < gs.boardSize and 0 <= row < gs.boardSize :
            if (row,col) in gs.possibleMoves():
                return (row,col)
            else: 
                return 0
        else:
            return 0