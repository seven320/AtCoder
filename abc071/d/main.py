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
S_1 = str(input())
S_2 = str(input())

dominos = []
i = 0
while i < N:
    if S_1[i] == S_2[i]:
        dominos.append(1)
        i += 1
    else:
        i += 2
        dominos.append(2)
ans = 1
for i, domino in enumerate(dominos):
    if i == 0:
        if dominos[i] == 1:
            ans *= 3
        else:
            ans *= 6
    else:
        if dominos[i] == dominos[i - 1] == 1 or dominos[i-1] == 1 and dominos[i] == 2:
            ans *= 2
            ans = ans % mod




        elif dominos[i] == dominos[i - 1] == 2:
        """
        R G       
        G (B or R)

        R B
        G R
        の3通り
        """
            ans *= 3
            ans = ans % mod

print(ans)
