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

N, K = LI()
h = [0 for i in range(N)]
for i in range(N):
    h[i] = int(input())

h.sort()
ans = mod
for i in range(N - K + 1):
    # print(h[i+K - 1] , h[i])
    ans = min(ans, h[i + K - 1] - h[i])
print(ans)