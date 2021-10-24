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

"""
#.#.#

.......
.#.###.
.#####.
.......


"""


H, W = LI()

S = []
for h in range(H):
    s = list(str(input()))
    S.append(s)

corners = [(0, 0), (1,0),(0, 1), (1,1)]
    
# black_corners = [
#     [(-1, 0), (1, 0), (0,1)],
#     [(-1, 0), (1, 0), (0, -1)],
#     [(0, 1), (0, -1), (1, 0)],
#     [(0, 1), (0, -1), (-1, 0)]
# ]
ans = 0
for h in range(H-1):
    for w in range(W-1):
        cnt = 0
        for (x, y) in corners:
            if S[h+y][w+x] == "#":
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
        

        


