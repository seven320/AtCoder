# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

W,H,N = map(int,input().split())
xya = [[] for i in range(N)]
for i in range(N):
    xya[i] = [int(i) for i in input().split()]

square = [[0 for i in range(W)] for i in range(H)]


for i in range(N):
    x,y,a = xya[i]
    if a == 1:
        for i in range(H):
            for j in range(x):
                square[i][j] = 1
    elif a == 2:
        for i in range(x,W):
            for j in range(H):
                square[j][i] = 1
    elif a == 3:
        for i in range(W):
            for j in range(y):
                square[j][i] = 1
    elif a == 4:
        for i in range(W):
            for j in range(y,H):
                square[j][i] = 1

black = 0
for i in range(H):
    black += sum(square[i])

print(H*W-black)
