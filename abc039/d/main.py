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
S = [0 for i in range(H)]
for i in range(H):
    S[i] = list(str(input()))

S_new = [[0 for i in range(W)] for j in range(H)]

for h in range(H):
    for w in range(W):
        pos = True
        for x in range(max(0, h - 1), min(H, h + 2)):
            for y in range(max(0, w - 1), min(W, w + 2)):
                if S[x][y] == ".":
                    pos = False

            if pos == False:
                break
        else:
            S_new[h][w] = 1
S_c = [[0 for i in range(W)] for j in range(H)]
for h in range(H):
    for w in range(W):
        if S_new[h][w]:
            for x in range(max(0, h - 1), min(H, h + 2)):
                for y in range(max(0, w - 1), min(W, w + 2)):
                    S_c[x][y] = 1
possible = True
for h in range(H):
    for w in range(W):
        if S[h][w] == "#" and S_c[h][w] == 1:
            pass
        elif S[h][w] == "." and S_c[h][w] == 0:
            pass
        else:
            possible = False
if possible:
    print("possible")
    change = {0:".", 1:"#"}

    for h in range(H):
        ans = []
        for w in range(W):
            ans.append(change[S_new[h][w]])
        print("".join(ans))

else:
    print("impossible")


            

