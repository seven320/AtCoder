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
N = int(input())
S = [0 for i in range(N)]
ans = {
    "AC":0,
    "WA":0,
    "TLE":0,
    "RE":0
}
for i in range(N):
    S[i] = str(input())
    ans[S[i]] += 1

for key in ans.keys():
    print(key + " x " + str(ans[key]))
"""
N = int(input())
S = []
for i in range(N):
    S.append(str(input()))

cnt = {
    "AC":0,
    "WA":0,
    "TLE":0,
    "RE":0
}
for s in S:
    cnt[s] += 1

for key in cnt.keys():
    print("{} x {}".format(key, cnt[key]))
