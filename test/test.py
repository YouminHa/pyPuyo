#!/usr/bin/env python3

# Run all tests

# app modules
import appPath
import lib.checkEnv

# test modules
import TestBlock
import TestPuyo

if __name__ == "__main__":
  TestBlock.TestBlock();
  TestPuyo.TestPuyo()

