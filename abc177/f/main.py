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

H, W = LI()
ab = []
for h in range(H):
    a, b = LI()
    a -= 1
    b -= 1
    ab.append((a,b))

cost = [0 for i in range(W)]
anss = [0 for i in range(H)]
for h in range(H+1):
    if h == H:
        break
    a, b = ab[h]
    for w in range(W):
        if a == 0:
            cost[0] = mod
        if a > 0:
            if a <= w <= b:
                cost[w] = cost[a - 1] + w - a + 2
            else:
                cost[w] = cost[w] + 1
    # print(cost)
    anss[h] = min(cost)

for h in range(H):
    if anss[h] >= mod:
        print(-1)
    else:
        print(anss[h])

    

