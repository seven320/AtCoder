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


ht = {}
for i in range(1, 10):
    for j in range(1, 10):
        ht[(i, j)] = 0

for i in range(N + 1):
    a = str(i)
    h, t = map(int, [a[0], a[-1]])
    if (h,t) in ht.keys():
        ht[(h,t)] += 1

# print(ht)
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += ht[(i, j)] * ht[(j, i)]

print(ans)