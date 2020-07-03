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
A = [[] for i in range(H)]
for i in range(H):
    a = list(str(input()))
    A[i] = a
# 複数のスタート地点が存在してもqueに突っ込むことで同様の効果が得られる．
visited = [[-1 for i in range(W)] for j in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            d.append((i,j))
            visited[i][j] = 0

moves = [[0,1],[1,0],[-1,0],[0,-1]]
cnt = 0
while len(d) > 0:
    X, Y = d.popleft()
    cnt = visited[X][Y]
    for x, y in moves:
        n_X = X + x
        n_Y = Y + y
        if 0 <= n_X < H and 0 <= n_Y< W:
            if visited[n_X][n_Y] == -1:
                visited[n_X][n_Y] = cnt + 1
                d.append((n_X, n_Y))
print(cnt)
