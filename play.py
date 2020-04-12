from tkinter import *
import time

from gui import gui

class play:
    def __init__(self,gameState):
        self.gs = gameState
        
    def run(self):
        if self.gs.guiOn:
            window = Tk()
            GUI = gui(window, self.gs)
            self.GUI = GUI
            GUI.window.bind("<Button-1>", lambda event: self.gamePlay(event,GUI), GUI)
            window.mainloop()
        else:
            self.gamePlay()
            
    def gamePlay(self,event=None,GUI=None):
        if GUI==None:
            print('GUI is off')    
        keepMakingMoves=True
        while keepMakingMoves:
            [move,keepMakingMoves] = self.playMove(event,GUI) #keep making moves unless it's a human's term (wrong move by human or bot just moved)
            if move==0:
                return
            self.gs.position[move]=self.gs.onMove #change position according to last move.
            self.gs.lastMove = move #set last move to move.
            if self.gs.guiOn: #if the GUI is on draw the new position.
                GUI.drawMove(move)
                GUI.window.update()
            gameover=self.gs.gameover() #See if someone has won.
            
            if gameover != 0:
                self.noMorePlay(GUI,self.gs.printWinner,gameover) #takes bool print winner
                return self.gs.onMove
            self.gs.onMove=3-self.gs.onMove 
            
    def playMove(self,event,GUI):
        if self.gs.ai[self.gs.onMove-1] == False: #if a human is on move
            move = self.gs.man.makeMove(self.gs, event, GUI.fromEdge, GUI.width)
            if move==0: 
                return [move,False]
        else: #bot is on move
            if self.gs.onMove==1:#first bot
                move = self.gs.bot.makeMove(self.gs)#bot 1 make move
            elif self.gs.onMove==2: #second bot
                move = self.gs.bot2.makeMove(self.gs)#bot 2 make move
            if self.gs.guiOn: time.sleep(self.gs.sleeptime) #slow down a bit after a bot move so you can view
            if self.gs.ai[2-self.gs.onMove] == False: #if the next player is a human exit this loop.
                return [move,False]
        return [move,True]
    
    def noMorePlay(self,GUI,printWinner,gameover):
        if printWinner:
            if gameover==1:
                print('Cross won!')
            elif gameover==2:
                print('Cricle won!')
            elif gameover==-1:
                print('draw!')
        if self.gs.guiOn:
            GUI.window.unbind("<Button-1>")
            
            
        