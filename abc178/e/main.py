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
xys = []
for i in range(N):
    x, y = LI()
    xys.append((x,y))

# 左下，左上，右上，右下

ans = 0
max_point = [0,0]
min_point = [mod, mod]

for i in range(N):
    x, y = xys[i]
    
    if sum(max_point) < (x + y):
        max_point = [x,y]
    if sum(min_point) > x + y:
        min_point = [x, y]

ans = abs(max_point[0] - min_point[0]) + abs(max_point[1] - min_point[1])

max_point = [0,0]
min_point = [mod, mod]

for i in range(N):
    x, y = xys[i]
    
    if sum(max_point) <= (-x + y):
        max_point_2 = [x,y]
    if sum(min_point) >= -x +y:
        min_point_2 = [x, y]

ans_2 = abs(max_point_2[0] - min_point_2[0]) + abs(max_point_2[1] - min_point_2[1])
# print(ans, ans_2)
print(max(ans, ans_2))