#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import constraint
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 1    
def Travellers(pairList):
  return constraint.Problem().getSolutions()


# Task 2
def CommonSum(n):
  return 0


from constraint import *
# Task 3
def MSquares(n, pairList):
  return constraint.Problem().getSolutions()


# Task 4
def PMSquares(n, pairList):
  return constraint.Problem().getSolutions()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# debug run
if __name__ == '__main__':
  if len(sys.argv) > 2:
    cmd = "{}({})".format(sys.argv[1], ",".join(sys.argv[2:]))
    print("debug run:", cmd)
    ret = eval(cmd)
    print("ret value:", ret)
    try:
      cnt = len(ret)
      print("ret count:", cnt)
    except TypeError:
      pass
  else:
    sys.stderr.write("Usage: {} <FUNCTION> <ARG>...\n".format(sys.argv[0]))
    sys.exit(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et ts=2 sw=2:
