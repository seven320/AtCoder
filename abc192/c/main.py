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

past = []

def g(a):
    elements = list(str(a))
    elements = [int(i) for i in elements]
    g_1 = sorted(elements)
    g_2 = sorted(elements, reverse=True)

    g_1 = [str(i) for i in g_1]
    g_2 = [str(i) for i in g_2]

    # print(int("".join(g_1)), int("".join(g_2)) )

    return int("".join(g_2)) - int("".join(g_1))

tmp = N
hoge = {}
for i in range(K):
    tmp = g(tmp)
    if tmp in hoge.keys():
        loop = i+1 - hoge[tmp]
        new_K = (K - i) % loop
        for i in range(new_K):
            tmp = g(tmp)
        break
    else:
        hoge[tmp] = i + 1


print(tmp)



