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

A, B, X = LI()

"""
Bについての数は一桁ずつ増えていくにしたがって増えるが，
Aは毎回増える．Bを基準にしつつ，Aを満たす数を探すべき
"""
ans = 0

for i in range(1,19):
    tmp = (X - i * B) // A 
    if tmp * A + len(str(tmp)) * B <= X:
        ans = max(ans, tmp)

# tmp = X // A
# if tmp * A + len(str(tmp)) * B <= X:
#     ans = max(ans, tmp) 


print(min(ans, 10 ** 9))



