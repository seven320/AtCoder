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

X, K, D = LI()

"""
X 
K回数 D移動
"""

X = abs(X)
tmp = X - D * K
if tmp <= 0:
    if X % D < abs(X % D - D):
        if (X - X % D) // D % 2 == K % 2:
            ans = X % D
        else:
            ans = abs(X % D - D)
    else:
        if (X - (X % D - D)) // D % 2 == K % 2:
            ans = abs(X % D - D)
        else:
            ans = X % D

else:
    ans = tmp

print(ans)
