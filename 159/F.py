# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 998244353
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, S = LI()
A = LI()

ans = 0
A_re = list(reversed(A))
dp = [[0 for i in range(10)] for j in range(N + 2)]
dp[0][0] = 1
for i in range(N):
    for j in range(S+1):
        dp[i + 1][j] += dp[i][j]
        if j - A_re[i] >= 0:
            dp[i + 1][j] += dp[i][j - A_re[i]]
print(dp)

for i in range(N + 1):
    for j in range(i, N + 1):
        print(dp[j][S] - dp[i][S])
        ans += dp[j][S] - dp[i][S]
print(ans)
