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

N, X = LI()

"""
Lv i のバーガーの厚みをa[i]
Lv i に含まれるパティの数をp[i]
とすると
a[0] = 1
a[i] = 2 * a[i-1] + 3
p[0] = 1
p[i] = 2 * p[i - 1] + 1

X = 1 f(N, X) = 0

1 < X <= 1 + a[i - 1]
一番したのバン

2 + a[i - 1] < X
一番したのバン　＋　
"""
a, p = [1], [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)

def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N - 1]:
        return f(N - 1, X - 1)
    else:
        return p[N - 1] + 1 + f(N - 1, X - 2 - a[N - 1])
print(f(N, X))





