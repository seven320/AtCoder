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
C_h, C_w = LI()
D_h, D_w = LI()

S = [[] for i in range(H)]
for h in range(H):
    S[h] = list(input())

visited = [[-1 for w in range(W)] for h in range(H)]
visited[C_h][C_w] = 0

moves = [[0,1],[1,0],[0,-1],[-1,0]]

p = (C_h,C_w)

cost = 0


for move in moves:
    x, y = p
    n_x = x + move[0]
    n_y = y + move[1]
    if 0 <= n_x < H and 0 <= n_y < W:
        if S[n_x][n_y] == ".":
            visited[n_x][n_y] = cost

if visited[D_h][D_w] != -1:
    ans = visited[D_h][D_w]