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

N = int(input())
A = LI()

"""

1 2 3 4

1*2, 1*3 1*4
2*3 2*4
3*4
1 6 3 5
1*6 1*3 1*5 = 1 * (6 + 3 + 5)
3*5 
10 ** 5 * 
"""
ans = 0
s = sum(A) % mod
for a in A:
    s -= a
    s %= mod
    ans += a * s % mod
    ans %= mod

print(ans)

    




