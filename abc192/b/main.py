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

S = list(str(input()))

ans = True

for i, s in enumerate(S):
    # print(i)
    # print(i, s)
    if i % 2 == 0:

        if s.islower():
            pass
        else:
            ans = False
    else:
        if s.isupper():
            pass
        else:
            ans = False

if ans:
    print("Yes")
else:
    print("No")