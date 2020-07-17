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

n = int(input())
a = LI()

"""
nCr = n!/(r! * (n-r)!)
なのでnは最大値をとりつつrはnの中間の値を撮るのが良さそう．
"""

a.sort()
o = a[-1]
diff = mod
for i in range(n):
    if diff > abs(a[i] - o / 2):
        p = a[i]
        diff = abs(a[i] - o / 2)
print(o,p)

