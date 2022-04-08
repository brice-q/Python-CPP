# Brice Hall
# Integrating Languages
# 4/7/2022

import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def MultiplicationTable(v):
    for i in range(1, 11):
        print(v, " x ", i, " = ", (v * i))
    return 0

def DoubleValue(v):
    return v * 2