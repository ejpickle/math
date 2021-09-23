#!/usr/bin/env python3
# sample of how to parse input arguments

# import the sys library
import sys

# sys.argv reads the command line input
# sample input:
#   python args.py x y z
# Parsing:
#   sys.argv[0] = args.py
#   sys.argv[1] = x
#   sys.argv[2] = y
#   sys.argv[3] = z

print(sys.argv[0])

print(sys.argv[1])

print(sys.argv[2])

print(sys.argv[3])
