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


"""
A_i * A_j + B_i * B_j = 0
の時選べない

Ai, Bi
1 5
5 -1
2 3
3 -2
4 1
1 1
1 -1
2 1
3 -6
"""


N = int(input())
for i in range(N):
    a,b = LI()
