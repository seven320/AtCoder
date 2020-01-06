# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
N,Q = LI()

lrt = [[] for i in range(Q)]
for i in range(Q):
    l,r,t = LI()
    l -= 1
    r -= 1
    lrt[i] = [l,r,t]

ans = [0 for i in range(N)]
for i in range(Q):
    l,r,t = lrt[i]
    ans[l:r+1] = [t for i in range(r - l + 1)]

for i in range(N):
    print(ans[i])
