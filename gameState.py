import numpy as np

from randomBot import *
from human import *

class gameState:
    def __init__(self):
        self.boardSize = 3
        self.winLength = 3
        self.man = human()
        self.bot = randomBot(self)
        self.bot2 = randomBot(self)
        self.ai = [False,False]
        self.guiOn = True
        if self.ai != [False,False]:
            self.Gui = True
        self.position = self.initPosition()
        self.onMove=1
        self.lastMove=[-1,-1]
        self.sleeptime=.1
        self.printWinner=True
    
    def initBfs(self):
        self.queue = [deque([]),deque([])]
        self.discovered = [[],[]]
    
    def gameover(self):
        if list(self.possibleMoves()) == []:
            return -1
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        y=self.lastMove[0]
        x=self.lastMove[1]
        for [dy,dx] in directions:
            for i in range(1,self.winLength):
                if(x+i*dx>=0 and x+i*dx<self.boardSize and y+i*dy>=0 and y+i*dy<self.boardSize):
                    # print(self.position[y+i*dy,x+i*dx],[i*dy,i*dx])
                    if self.position[y+i*dy,x+i*dx] != self.onMove:
                        break
                    if i == self.winLength-1:
                        return self.onMove
                else:
                    break
        return False
            
    def initPosition(self):
        return np.zeros((self.boardSize,self.boardSize))
        
    def possibleMoves(self):
        return zip(*np.nonzero(self.position==0))
        
    def resetGameState(self):
        self.position = self.initPosition()