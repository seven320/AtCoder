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

N, M = LI()
A = LI()

"""
WWBWWWWBW

K 1 ~ min(W_width)
K 大きい方が良い？

ex1
BWBWW
K = 1, ans = 3

ex2
WWBWWWWWBWWWB
K = 2, ans = 6

exadd
WWBBBBWW
8 4
6 3 4 5


"""
if M == 0:
    print(1)
    sys.exit()
if M == N:
    print(0)
    sys.exit()


k = mod
A.sort()
left = 0
for i in range(M):
    if A[i] - left - 1 > 0:
        k = min(A[i]-left-1, k)
    left = A[i]

if A[-1] != N:
    k = min(k, N - A[-1])
if A[0] != 1:
    k = min(k, A[0] - 1)
ans = 0
left = 0
for i in range(M):
    if A[i] - left -1> 0:
        ans += math.ceil((A[i] - left - 1)/k)
    left = A[i]
if N - A[-1] > 0:
    ans += math.ceil((N - A[-1]) / k)

print(ans)