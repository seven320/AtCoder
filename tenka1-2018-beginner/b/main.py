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

A, B, K = LI()

for k in range(K):
    if k % 2 == 0:
        if A % 2 == 1:
            A -= 1
        c = A // 2
        A -= c
        B += c
    else:
        if B % 2 == 1:
            B -= 1
        c = B // 2
        B -= c
        A += c
    
print(A, B)
