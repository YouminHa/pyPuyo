#!/usr/bin/env python3
# test.py
# Run all testcases in the directory

import glob, os, unittest

import appPath
import lib.checkEnv

def runAllTestCases():
  # change to current directory
  os.chdir(os.path.dirname(os.path.abspath(__file__)))

  # Run all test modules
  testFiles = glob.glob('Test*.py')
  moduleNames = [ os.path.splitext(os.path.basename(fileName))[0] for fileName in testFiles ]
  suites = [ unittest.defaultTestLoader.loadTestsFromName(m) for m in moduleNames ]
  ts = unittest.TestSuite(suites)
  tr = unittest.TextTestRunner().run(ts)

if __name__ == '__main__':
  runAllTestCases()

