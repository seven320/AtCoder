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
A = LI()
Q = int(input())


move_dic = {}
revers_move_dic = {}
for i in range(1,10**5):
    revers_move_dic[i] = -1

BC = [() for i in range(Q)]
for q in range(Q):
    BC[q] = LI()


anss = []
A_collections = collections.Counter(A)

# print(A_collections)
ans = sum(A)
for q in range(Q):
    b,c = BC[q]

    if b in A_collections.keys():
        A_collections[c] += A_collections[b]
        ans += (c - b) * A_collections[b]
        A_collections[b] = 0
    print(ans)

    
