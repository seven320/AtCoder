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
wv = [[] for i in range(N)]
for i in range(N):
    wv[i] = [int(i) for i in input().split()]

W = int(input())
print(wv)

dp = [[0 for j in range(W+1)] for i in range(N+1)]
for i in range(N):
    w,v = wv[i]
    for j in range(W):
        if j < w:
            dp[i+1][j] = dp[i][j]
        if j+w <= W:
            dp[i+1][j+w] = max(dp[i][j+w],dp[i+1][j]+v)


print(max(dp[-1]))
print(dp)
