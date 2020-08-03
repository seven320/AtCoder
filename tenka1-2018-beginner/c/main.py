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
A = []
for i in range(N):
    A.append(int(input()))

A.sort()
# 真ん中がmax
left = A[-1]
right = A[-1]
tmp = 0
cnt = 0
while cnt != N - 1:
    if cnt % 4 == 2:
        tmp += abs(right - A[N - 2 - cnt // 4])
        right = A[N - 2 - cnt // 4]
    elif cnt % 4 == 3:
        tmp += abs(left - A[N - 2 - cnt // 4 - 1])
        left = A[N - 2 - cnt // 4 - 1]
    elif cnt % 4 == 0:
        tmp += abs(right - A[cnt // 4])
        right = A[cnt // 4]
    else:
        tmp += abs(left - A[cnt // 4 + 1])
        left = A[cnt // 4 + 1]
    cnt += 1

ans = tmp
print(ans)
# 真ん中がmin
left = A[0]
right = A[0]
tmp = 0
cnt = 0
while cnt != N - 1: 
    if cnt % 4 == 0:
        tmp += abs(right - A[N - 1 - cnt // 4])
        right = A[N - 1 - cnt // 4]
    elif cnt % 4 == 1:
        tmp += abs(left - A[N - 1 - cnt // 2 - 1])
        left = A[N - 1 - cnt // 4 - 1]

    elif cnt % 4 == 2:
        tmp += abs(right - A[cnt // 4 + 1])
        right = A[cnt // 4 + 1]
    else:
        tmp += abs(left - A[cnt // 4 + 2])
        left = A[cnt // 4 + 2]
    print(right, left)
    cnt += 1
ans = max(tmp, ans)
print(ans)


