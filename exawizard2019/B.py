# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える


n = int(input())
s = str(input())

rb = [0,0]
for i in s:
    if i == "R":
        rb[0] += 1
    else:
        rb[1] += 1

if rb[0] > rb[1]:
    print("Yes")
else:
    print("No")
