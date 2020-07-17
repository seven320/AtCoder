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

N, M, X = LI()
A = LI()

left = 0
right = 0

cs = [0 for i in range(N)]
for a in A:
    cs[a] = 1
for i in range(X):
    if cs[i]:
        left += 1

for i in range(X, N):
    if cs[i]:
        right += 1

print(min(left, right))