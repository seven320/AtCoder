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

# X = int(input())
# if 599 >= X:
#     ans = 8
# elif 600 <= X <= 799:
#     ans = 7
# elif 800 <= X <= 999:
#     ans = 6
# elif 1000 <= X <= 1199:
#     ans = 5
# elif 1200 <= X <= 1399:
#     ans = 4
# elif 1400 <= X <= 1599:
#     ans = 3
# elif 1600 <= X <= 1799:
#     ans = 2
# else:
#     ans = 1
# print(str(ans))

X = int(input())
print(8 - (X - 400) // 200)