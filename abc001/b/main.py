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

m = int(input())

if m < 100:
    vv = "00"
elif 100 <= m <= 5000:
    vv = str(int(m / 1000 * 10)).zfill(2)
elif 6000 <= m <= 30000:
    vv = str(m // 1000 + 50)
elif 35000 <= m <= 70000:
    vv = (m // 1000 - 30) // 5 + 80
elif 70000 < m:
    vv = "89"

print(vv)