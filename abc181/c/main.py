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
ans = False
xys = []
for i in range(N):
    x, y = LI()
    xys.append((x,y))

for i in range(N):
    x_0, y_0 = xys[i]
    for j in range(i+1, N):
        x_1, y_1 = xys[j]
        for k in range(j+1, N):
            x_2, y_2 = xys[k]
            if x_2 == x_1 == x_0:
                ans = True
                # print(x_2, x_1, x_0)
            elif y_2 == y_1 == y_0:
                ans = True
                # print(y_0, y_1, y_0)
            if(x_1-x_0)!=0 and (y_1-y_0) != 0:
                if (x_2 - x_1) / (x_1-x_0) == (y_2 - y_1)/(y_1-y_0):
                    ans = True
if ans:
    print("Yes")
else:
    print("No")