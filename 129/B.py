# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
W = [int(i) for i in input().split()]

L = [-1 for i in range(N+1)]
R = [-1 for i in range(N+1)]
for i in range(1,N+1):
    L[i] = sum(W[:i])
    R[i] = sum(W[i:])

ans = mod
for i in range(1,N+1):
    ans = min(ans,abs(L[i]-R[i]))


print(ans)
