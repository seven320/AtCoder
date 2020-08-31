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

K = int(input())
amari = []
s = 0
before = 0
for i in range(10 ** 6 + 1):
    if i == 0:
        s += 7 % K
        before = 7 % K
    else:
        before = before * 10 % K
        s += before
    s = s % K
    if s == 0:
        break
else:
    print("-1")
    sys.exit()

print(i + 1)






"""
7
77
777
7777

7
70 == 7 * 10 =
700 ==  



1
11
111
1111

k = 3
1 == 1
10 == 1
100 == 1

k = 4
1 == 1
10 == 2
100 == 0
100 == 10 * 10 == 2 * 10
"""
