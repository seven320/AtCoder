# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


N,M = map(int,input().split())
a = [0 for i in range(M)]
for i in range(M):
    a[i] = int(input())

miss_stairs = [0 for i in range(N)]
for i in range(M):
    miss_stairs[a[i]-1] = 1


dp = [0 for i in range(N+1)]
dp[0] = 1
if miss_stairs[0] == 1:
    dp[1] = 0
else:
    dp[1] = 1
for i in range(N-1):
    if miss_stairs[i+1] == 0:
        dp[i+2] = (dp[i] + dp[i+1]) % mod
# print(dp)

print(dp[-1]% mod)
