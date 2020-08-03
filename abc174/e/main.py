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
A = LI()

A.sort()
# 割る回数を保存していき，破られた後も最大のものにたいして，足していく
logs = [0 for i in range(N)]
submax_A = A[-2]
cnt = 0
tmp = 0
while cnt > K:
    tmp = logs
    if submax_A > A[-1] // logs[-1]:


    cnt += 1
    



"""
L > t, L - t



7,9

3.5, 3.5, 9

3.5, 3.5, 3, 3, 3

K = 1
7, 4.5, 4.5
K = 2
3.5, 3.5, 4.5, 4.5
K = 3
3.5, 3.5, 3, 3, 3

K = 4
2.3, 2.3, 2.3, 3,3,3

"""