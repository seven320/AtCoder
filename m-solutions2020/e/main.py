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
xyp = []
for i in range(N):
    xyp.append(LI())
# xyp = sorted(xyp, key=lambda xyp: xyp[2], reverse= True)
def cal_work(x_lines, y_lines):
    work = 0
    for i in range(N):
        min_dis = mod
        x, y, p = xyp[i]
        for x_line in x_lines:
            min_dis = min(min_dis, abs(x_line - x))
            if min_dis == 0:
                break
        for y_line in y_lines:
            min_dis = min(min_dis, abs(y_line - y))
            if min_dis == 0:
                break
        work += min_dis * p
    return work

def n2kdigit(n,k):
    digits = [0 for i in range(N)]
    cnt = 0
    while n > 0:
        digits[cnt]= n % k
        n = n // k
        cnt += 1
    return digits

anss = [float("inf") for i in range(N + 1)]
for i in range(3 ** N):
    digits = n2kdigit(i, 3)
    x_lines = [0]
    y_lines = [0]
    for i, digit in enumerate(digits):
        if digit == 0:
            pass
        elif digit == 1:
            x_lines.append(xyp[i][0])
        else:
            y_lines.append(xyp[i][1])
            
    cnt = len(x_lines) + len(y_lines) - 2
    anss[cnt] = min(anss[cnt], cal_work(x_lines, y_lines))

for ans in anss:
    print(ans)
    

    

            

