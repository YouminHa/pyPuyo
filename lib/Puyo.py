'''
Puyo.py

Main routine
'''
from .Block import Block
from .Board import Board


class Puyo:
  '''
  Main class
  '''
  def __init__(self, boardWidth = 6, boardHeight = 12):
    self.board = Board(boardWidth, boardHeight)

  def newBlock(self, b1, b2):
    ''' Get 2 new blocks on top '''
    self.b1, self.b2 = b1, b2
    # Set x position
    self.b1.pos = {'x':1, 'y':1}
    self.b2.pos = {'x':2, 'y':1}

  def land(self):
    ''' Land current floating blocks '''
    pass

  def maxHeight(self):
    ''' Return current max height on the board '''
    return self.board.maxHeight()

  def run(self):
    ''' run the loop '''
    pass

