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

N, K = LI()
P = LI()
C = LI()

for i in range(N):
    P[i] -= 1

"""
C_0 C_1 C_2 C_3 ...
dp cost?
移動回数？


  0 1   2       3
0 l p0 p0 + p1 p0+p1+p2
1 
2
3





"""

loop_cost = sum(C)
cost_table = []
next_p= 0
cost = 0
for i in range(N + 1):
    next_p = P[next_p]
    cost += C[next_p]
    cost_table.append(cost)

print(cost_table)

