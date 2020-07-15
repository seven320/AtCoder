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

anss = [0 for i in range(N + 1)]
for x in range(1, int(math.sqrt(N))):
    for y in range(1, int(math.sqrt(N))):
        for z in range(1, int(math.sqrt(N))):
            tmp = x ** 2 + y ** 2 + z ** 2 + x*y + x*z + y*z
            if tmp <= N:
                anss[tmp] += 1 

for i in range(1, N + 1):
    print(anss[i])