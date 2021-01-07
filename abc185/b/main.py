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
AB = []

N, M, T = LI()
for m in range(M):
    a,b = LI()
    AB.append((a,b))

status = N
l_time = 0
ans = True
for m in range(M):
    a,b = AB[m]
    if status - (a - l_time) <= 0:
        ans = False
        break
    status =  min(status - (a - l_time) + (b-a), N)
    l_time = b

if status - (T - l_time) <= 0:
    ans = False
if ans:
    print("Yes")
else:
    print("No")
