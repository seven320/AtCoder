# encoding:utf-8
import copy
import numpy as np
import random

n = int(input())

mappings = []

for i in range(n):
    mapping = [int(i) for i in input().split()]
    mappings.append(mapping)

for cx in range(101):
    for cy in range(101):
        H = -1
        for i in range(n):
            x,y,h = mappings[i]
            if h != 0 and H == -1:
                H = h+abs(x-cx)+abs(y-cy)
            elif h != 0 and H!=h+abs(x-cx)+abs(y-cy):
                break

            if i == len(mappings)-1:
                ans = (cx,cy,H)

cx,cy,H = ans
print(cx,cy,H)
