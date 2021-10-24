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

ab = []
for i in range(N):
    ab.append(LI())
#task1の最適解

ans = mod
for i in range(N):
    for j in range(N):
        if j == i:
            continue
        ans = min(ans, max(ab[i][0], ab[j][1]))

ans2 = mod
for i in range(N):
    ans2 = min(sum(ab[i]), ans2)

# print(ans, ans2)
print(min(ans, ans2))

