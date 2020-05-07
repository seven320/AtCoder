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
d = [0 for i in range(K)]
A = [[] for i in range(K)]
for k in range(K):
    d[k] = int(input())
    A[k] = LI()

sunuke = [0 for i in range(N)]
for k in range(K):
    for s in A[k]:
        sunuke[s - 1] += 1

ans = 0
for s in sunuke:
    if s == 0:
        ans += 1
print(ans)
    