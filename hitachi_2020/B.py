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

A, B, M = LI()
a = LI()
b = LI()
xyc = [[] for i in range(M)]
for i in range(M):
    x, y, c = LI()
    x -= 1
    y -= 1
    xyc[i] = [x, y, c]

ans = mod
for i in range(M):
    x, y, c = xyc[i]
    ans = min(ans, a[x] + b[y] - c)

ans = min(ans, min(a) + min(b))
print(ans)
