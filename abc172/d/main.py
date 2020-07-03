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
N 

1 * f(1) + 2 * f(2) + ...


N = 4
f(1) = 1
f(2) = 2
f(3) = 2
f(4) = 3
f(5) = 2
f(6) = 4
f(7) = 2
f(8) = 1,2,4,8 = 4
f(9) = 1, 3, 9 = 3
f(10) = 1, 2, 5, 10 = 4


f(x * y) = f(x) + f(y) - f(x or y)
f(10) = 2 + 2 - 1 + 1= 3
f(11) = 2
f(12) = f(2) + f(6) = 2 + 4 = 6?
f(12) = 1, 2,3,4,6,12

"""
dp = [0 for i in range(10 ** 7 + 1)]
dp[1] = 1
dp[2] = 2

N = int(input())

