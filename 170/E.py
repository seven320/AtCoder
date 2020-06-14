# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, Q = LI()

members = [0 for i in range(N)]
gardens = [[] for i in range(2 * 10 ** 5)]

ab = [[] for i in range(N)]
for i in range(N):
    a, b = LI()
    b -= 1
    gardens[b].append(a)
    ab[i] = [a,b]

ad = [[] for i in range(N)]
cd = [[] for i in range(N)]
for i in range(Q):
    c,d = LI()
    c -= 1
    d -= 1
    cd[i] = [c, d]
    rate = ab[c][0]
    ad[i] = [rate, d]

for garden in gardens:
    garden.sort()

ave = mod
for garden in gardens:
    if len(garden) > 0:
        ave = min(ave, garden[-1])
