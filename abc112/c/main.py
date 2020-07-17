#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
xyh = []
for i in range(N):
    x, y, h = LI()
    xyh.append([x, y, h])


"""

C_x C_y H

XYの高度はmax(H - abs(X - C_x) - abs(Y - C_y), 0)
"""
xyh = sorted(xyh, key=lambda xyh: xyh[2], reverse=True)

# print(xyh)
ans = (0,0,0)
for c_x in range(101):
    for c_y in range(101):
        H = 0
        flag = True
        for i, (x, y, h) in enumerate(xyh):
            if i == 0:
                H = h + abs(x - c_x) + abs(y - c_y)
            if h != max(H - abs(x - c_x) - abs(y - c_y), 0):
            # if H != max(h + abs(x - c_x) + abs(y - c_y), 0):
                flag = False
        if flag:
            ans = (c_x, c_y, H)
    
X, Y, H = ans
print(X, Y, H)

