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
dp
time / books_no?
10 0 0
20 0 0
30 0 0
40 0 0
50 0 0
60 1 0
70 1 0
80 0 1




"""



N, M, K = LI()
A = LI()
B = LI()

"""
片方に注目して探索すればよい　

単純にfor,forだと計算量がまずいが，前回の値の部分から探索すればいいのでそこまで
計算量は増えない

"""

a = [0]
b = [0]

for i in range(N):
    a.append(a[-1] + A[i])

for i in range(M):
    b.append(b[-1] + B[i])

# print(a)
ans = 0
j = M
for i in range(N + 1):
    if a[i] > K:
        break
    while b[j] > K - a[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
    