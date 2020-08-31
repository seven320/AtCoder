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

# A, B, C = LI()
# K = int(input())

# for k in range(K):
#     if A < B:
#         C *= 2
#     else:
#         B *= 2

# if A < B and B < C:
#     print("Yes")
# else:
#     print("No")
A, B, C = LI()
K = int(input())

for k in range(K):
    if A >= B:
        B *= 2
    else:
        C *= 2

if A < B < C:
    print("Yes")
else:
    print("No")