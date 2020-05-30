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

dp = [[0 for i in range(K + 1)] for j in range(N+1)]
# dp 
# dp[i][j]
# iは桁数目
# j は幾つの値か
for k in range(K):
    dp[0][k] = 1

for n in range(N - 1):
    for k in range(K):
        for tmp in range(1, K+1):
            dp[n+1][math.gcd(tmp, dp[n][k])] = (dp[n][k] + dp[n+1][math.gcd(tmp, dp[n][k])]) % mod

print(dp)
ans = sum(dp[-1]) % mod
print(ans)



"""
N, K = 3,2

111
112
121
122
211
212
221
222

"""