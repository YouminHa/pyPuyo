'''
Block.py

A Block
'''
from enum import Enum


# Block color
class Color(Enum):
  RED     = 1
  GREEN   = 2
  BLUE    = 3
  YELLOW  = 4
  PURPLE  = 5
  ICE     = 99


# A puyo block
class Block:
  def __init__(self, color):
    self.color = Color(color)


# Ice block
class IceBlock(Block):
  def __init__(self, color, life):
    self.life = life

