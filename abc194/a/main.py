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

A, B = LI()

if A+B >= 15 and B >= 8:
    ans = 1
elif A+B >= 10 and B >= 3:
    ans = 2
elif A+B >= 3:
    ans = 3
else:
    ans = 4

print(ans)