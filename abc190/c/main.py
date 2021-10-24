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
N, M = LI()

ABs = []
for i in range(M):
    a, b = LI()
    a -= 1
    b -= 1
    ABs.append([a,b])
K = LI()[0]
cds = []
for i in range(K):
    c,d = LI()
    c -= 1
    d -= 1
    cds.append([c,d])

def count(plates):
    ans = 0
    for (a,b) in ABs:
        if plates[a] > 0 and plates[b] > 0:
            ans += 1
    return ans

ans = 0
for i in range(2 ** K):
    cnt = 0
    plates = [0 for i in range(N)]
    for j in range(K):
        if i % 2 == 0:
            plates[cds[j][0]] += 1
        else:
            plates[cds[j][1]] += 1
        i = i // 2
    ans = max(count(plates), ans)
print(ans)

    
    

