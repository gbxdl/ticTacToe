from tkinter import *
import PIL.Image
from PIL import ImageTk

class gui:
    
    def __init__(self,window,gameState):
        self.canvasWidth = 800
        self.canvasHeight = 800
        self.window = window
        self.window.title('Tic Tac Toe')
        self.gs = gameState
        self.width = self.canvasHeight / (self.gs.boardSize+2)
        self.fromEdge=self.width
        self.drawCanvas()
        self.loadImages()
        
    def drawMove(self,move):
        locrow = self.canvasWidth*(move[0]+.5)/(self.gs.boardSize+2) + self.fromEdge
        loccol = self.canvasWidth*(move[1]+.5)/(self.gs.boardSize+2) + self.fromEdge
        if self.gs.onMove==1:
            self.canvas.create_image(loccol,locrow,image=getattr(self,'cross'))
        if self.gs.onMove==2:
            self.canvas.create_image(loccol,locrow,image=getattr(self,'circle'))
        
    def drawCanvas(self):
        self.canvas=Canvas(self.window,width=self.canvasWidth,height=self.canvasHeight)
        self.canvas.pack()
        self.drawField()
        self.restartButton(self.gs)
    
    def drawField(self):
        for iSquare in range(1,self.gs.boardSize):
            x1 = self.fromEdge+iSquare*self.width
            y1 = self.fromEdge
            x2 = self.fromEdge+iSquare*self.width
            y2 = self.canvasHeight - self.fromEdge
            self.canvas.create_line(x1,y1,x2,y2)
            self.canvas.create_line(y1,x1,y2,x2)
            
    def restartButton(self,gameState):
        self.resetButton = Button(self.window, text="New game",command = lambda: self.restart(gameState))
        self.resetButton.pack(side=LEFT)
    
    def restart(self,gameState):
        gameState.resetGameState()
        self.canvas.destroy()
        self.resetButton.destroy()
        self.drawCanvas()
        
    def loadImages(self):
        cross = PIL.Image.open('cross.gif')
        circle = PIL.Image.open('circle.gif')
        frac = .58
        width = int(frac*self.width)
        height = int(frac*self.width)
        self.cross = ImageTk.PhotoImage(cross.resize((height,width),PIL.Image.ANTIALIAS))
        self.circle = ImageTk.PhotoImage(circle.resize((height,width),PIL.Image.ANTIALIAS))