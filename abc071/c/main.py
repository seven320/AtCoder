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

A_collection = collections.Counter(A)
bars = []
for key in A_collection.keys():
    if A_collection[key] > 1:
        bars.append(key)

ans = 0
bars.sort(reverse = 1)
if len(bars) > 1:
    ans = bars[0] * bars[1]
    if A_collection[bars[0]] > 3:
        ans = bars[0] ** 2
print(ans)
