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

L = int(input())

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

print(cmb((L-1), 11))


# mod = 10 ** 9 + 7
# n_ = 10 ** 5 + 3 # まで対応

# fun = [1 for i in range(n_+1)]
# for i in range(1, n_ + 1):
#     fun[i] = fun[i-1] * i % mod

# rev = [1 for i in range(n_+1)]
# rev[n_] = pow(fun[n_], mod-2, mod)
# for i in range(n_-1,0,-1):
#     rev[i] = rev[i+1]*(i+1) % mod

# def nCr(n,r):
#     if n <= 0 or r < 0 or r> n:return 0
#     return fun[n]*rev[r]%mod*rev[n-r]%mod

# print(nCr(L-1, 11))