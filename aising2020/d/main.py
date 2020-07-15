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

# N = int(input())
# X = str(input())

N = 10 ** 5
X = "1" * 10 ** 5
def popcount(x):
    z = x.count("1")
    return int(x, 2) % z

for i in range(N):
    if X[i] == "1":
        c = "0"
    else:
        c = "1"
    x = X[:i] + c + X[i + 1:]
    ans = 0
    while True:
        ans += 1
        x = bin(popcount(x))[2:]
        if x == "0":
            break
    print(ans)


