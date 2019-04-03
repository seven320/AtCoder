# encoding:utf-8
import copy
import numpy as np
import random


X,Y = map(str,input().split())

if X > Y:
    ans = ">"
elif X < Y:
    ans = "<"
else:
    ans = "="

print(ans)
