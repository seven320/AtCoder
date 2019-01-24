# encoding:utf-8

import numpy as np
import random

A,B,C,D = map(int, input().split())
if A+B > C+D:
    print("Left")
elif A+B == C+D:
    print("Balanced")
else:
    print("Right")
