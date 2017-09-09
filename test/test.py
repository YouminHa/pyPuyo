#!/usr/bin/env python3
# test.py
# Run all tests

import unittest

import appPath
import lib.checkEnv

# test modules
import TestBlock
import TestPuyo

# Test collection
tests = (
    TestBlock.TestBlock(),
    TestPuyo.TestPuyo()
    )

# Run all tests!
if __name__ == "__main__":
  ts = unittest.TestSuite()
  ts.addTests(tests)
  unittest.TextTestRunner().run(ts)
