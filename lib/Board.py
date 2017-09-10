'''
Board.py

Game board
'''
from .Block import Block, Color, IceBlock

class Board:
  def __init__(self, width, height):
    self.width, self.height = width, height
    self.cols = ([],) * self.width

  def maxHeight(self):
    ''' Get the len of longest list in cols '''
    return len(max(self.cols, key=len))

