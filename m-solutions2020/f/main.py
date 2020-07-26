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
import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
pos = {
    "U":[],
    "R":[],
    "D":[],
    "L":[]
    }
xyu =[]
for i in range(N):
    x, y, u = input().split()
    x = int(x)
    y = int(y)
    u = str(u)
    xyu.append([x,y,u])

direction = {
    "U":[0,1],
    "D":[0, -1],
    "R":[1, 0],
    "L":[-1,0]
}
directions = np.zeros((N, 2))
positions = np.zeros((N, 2))
for i, (x, y, u) in enumerate(xyu):
    if u == "U":
        directions[i, 1] = 1
    elif u == "D":
        directions[i, 1] = -1
    elif u == "R":
        directions[i, 0] = 1
    else:
        directions[i, 0] = -1
    positions[i, 0] = x
    positions[i, 1] = y


ans = -1
for time in range(1, 200000):
    positions += directions
    positions.tolist()

    if len(set(positions.tolist())) < N:
        ans = time
        break
if ans == -1:
    print("SAFE")
else:
    print(ans)

