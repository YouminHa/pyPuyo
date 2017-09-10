import unittest

import appPath
from lib.Puyo import Puyo
from lib.Block import Block, Color

class TestPuyo(unittest.TestCase):
  def testHeight(self):
    p = Puyo()

    # 1st block
    p.newBlock(Block(Color.RED), Block(Color.BLUE))
    p.land()
    self.assertEqual(1, p.maxHeight(), "1st block")

    # more block
    p.newBlock(Block(Color.RED), Block(Color.RED))
    p.land()
    self.assertEqual(2, p.maxHeight(), "2nd block over 1st block")


