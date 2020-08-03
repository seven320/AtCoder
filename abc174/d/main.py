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
c = list(str(input()))

cs = [0 for i in range(N)]
for i,color in enumerate(c):
    if color == "R":
        cs[i] = 1

ans = min(sum(cs), N - sum(cs))
tmp = sum(cs)


count = 0
for i in range(tmp):
    if cs[i]:
        count += 1

ans = min(ans, tmp - count)
print(ans)




"""
out 
WR



ok
RRRRRWWWWW 入れ替える
RRRRRR 全てRにする
WWWWWW 全てWにする


1100

1110111000

tmp = 6


"""