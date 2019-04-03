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
            if done == False:
                break
            x,y,h = mappings[i]
            if h == 0:
                pass
            else:
                if H == -1:
                    H = h+abs(x-cx)+abs(y-cy)
                elif H!=h+abs(x-cx)+abs(y-cy):
                    done = False
                    
            if i == len(mappings)-1:
                    ans = (cx,cy,H)

cx,cy,H = ans
print(cx,cy,H)
