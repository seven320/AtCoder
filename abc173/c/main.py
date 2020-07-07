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
"""
H, W, K = LI()
c = [[0 for j in range(W)] for i in range(H)]

for h in range(H):
    c[h] = list(str(input()))

# print(c)
for h in range(H):
    for w in range(W):
        if c[h][w] == ".":
            c[h][w] = 0
        else:
            c[h][w] = 1 


"""
# 2 ** (H + W)通り試せば良い
"""
ans = 0
# 10進数のnを2進数のリストに変換


def n2kdigit(n,k):
    digits = [0 for i in range(H + W)]
    tmp = 0
    while n > 0:
        digits[tmp] = n % k
        n = n // k
        tmp += 1

    return digits

for i in range(2 ** (H + W)):
    cnt = 0
    c_ = copy.deepcopy(c)
    digits = n2kdigit(i, k = 2)
    for j, digit in enumerate(digits):
        if digit == 1:
            if j >= H:
                for h in range(H):
                    # print(j - H -1)
                    c_[h][j - H - 1] = 0
            else:
                "Hを示す"
                c_[j] = [0 for k in range(W)]
    # print(c_)
    for h in range(H):
        cnt += sum(c_[h])
    if cnt == K:
        ans += 1

print(ans)


"""

# 実装例
H, W, K = list(map(int, input().split()))

c = []
for h in range(H):
    l = []
    for s in input():
        if s == ".":
            l.append(0)
        else:
            l.append(1)
    c.append(l)

ans = 0
for bit_h in range(2 ** H): # bit_hが2進数で隠すか隠さないかを示す
    for bit_w in range(2 ** W):
        k = 0
        nn = np.asarray(c)
        # mask 部分
        for h in range(H):
            """
            (bit_h & 2 ** h)の部分で，マスクがかかっている部分を調べる
            >> hによって，参照したい行が0 or 1なのかを調べる．0なら色がないので，したの作業がいらない
            """
            if (bit_h & 2 ** h) >> h == 0:
                continue
            nn[h] = np.zeros((1, W))
        for w in range(W):
            if (bit_w & 2 ** w) >> w == 0:
                continue
            nn[:, w] = np.zeros((1, H))
        # cnt部分
        if K == np.sum(nn):
            ans += 1
print(ans)

        


        
