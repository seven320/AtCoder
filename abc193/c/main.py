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

N = int(input())

anss = []

for i in range(2, int(math.sqrt((N)))+1):
    for j in range(2, N):
        if i ** j <= N:
            anss.append(i**j)
        else:
            break

print(N - len(set((anss))))
