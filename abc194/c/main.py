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

# 2 * a_i * a_j
# 2 * (a_0 * a_1 + a_0 * a_2 + a_1 * a_2) = 2 * (a_0 * sum(a) - a_0 + )

N = int(input())
A = LI()

ans = 0
for i in range(N):
    ans += A[i] ** 2 * (N - 1)

# 4 + 64 + 4 + 16 + 64 + 16

sum_A = sum(A)
for i in range(N):
    ans -= A[i] * (sum_A - A[i])

print(ans)



