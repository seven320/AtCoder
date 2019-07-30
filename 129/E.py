# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

L = str(input())
n = len(L)
dp = [[0,0] for i in range(n+1)]
dp[0][0] = 1
for i in range(n):
    if L[i] == "0": #a+b = 0
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = (dp[i][1] + dp[i][1]*2) % mod
    else:
        dp[i+1][0] = dp[i][0] * 2 % mod
        dp[i+1][1] = (dp[i][0] + dp[i][1] + dp[i][1]*2) % mod


print(sum(dp[n]) % mod)
