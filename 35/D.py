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

N,M,T = LI()
A = LI()
abc = [[] for i in range(M)]
for i in range(M):
    a,b,c = LI()
    a -= 1
    b -= 1
    abc[i] = [a,b,c]

dp = [[mod for i in range(N)] for j in range(N)]
for i in range(M):
    a,b,c = abc[i]
    dp[a][b] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
