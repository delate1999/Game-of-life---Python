# class which defines cell #
# it also creates graphic window #
from graphics import *

win = GraphWin("My Window", 500, 500,autoflush=False)
win.setBackground('black')


class Cell:
    def __init__(self,x,y,state,mates):
        self.x = x
        self.y = y
        self.state = state
        self.mates = mates


    def draw_cell(self):
        square = Rectangle(Point(self.x-5,self.y-5), Point(self.x+5,self.y+5))
        if self.state == 'alive':
            square.setFill('white')
        if self.state == 'dead':
            pass #square.setFill('black')
        square.draw(win)