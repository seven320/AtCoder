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

S = str(input())
T = str(input())

max_cnt = 0
for i in range(len(S) - len(T) + 1):
    cnt = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            cnt += 1

        
    max_cnt = max(cnt, max_cnt)

print(len(T) - max_cnt)

