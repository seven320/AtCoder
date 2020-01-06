# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

H, W = LI()
a = []
for h in range(H):
    a.append(LI())

# print(a)

memo = [[-1 for i in range(W+1)] for j in range(H+1)]

def search(h,w):
    val = a[h][w]
    moves = [[0,1],[1,0],[-1,0],[0,-1]]
    ret = 1
    for move in moves:
        x,y = move
        n_h = h + x
        n_w = w + y
        if -1 < n_h < H and -1 < n_w < W:
            check = True
            if a[n_h][n_w] > val:
                if memo[n_h][n_w] == -1:
                    ret = (ret + search(n_h, n_w)) % mod
                else:
                    ret = (ret + memo[n_h][n_w]) % mod
    memo[h][w] = ret
    return ret

ans = 0
for h in range(H):
    for w in range(W):
        if memo[h][w] == -1:
            ans = (ans + search(h,w)) % mod
        else:
            ans = (ans + memo[h][w]) % mod
print(ans)
