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

N, K = LI()
p = LI()
ps = []
for i in range(N):
    ps.append((p[i] + 1) / 2)

anss = []
tmp = 0
for i in range(N):
    tmp += ps[i]
    if i > K - 1:
        tmp -= ps[i - K]
    anss.append(tmp)

print(max(anss))
