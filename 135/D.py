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

S = list(str(input()))
S.reverse()
extra = 0
each_extras = [[] for i in range(S.count("?"))]
cnt = 0
mul = 1
for i in range(len(S)):
    if S[i] == "?":
        each_extras[cnt] = []
        for x in range(10):
            each_extras[cnt].append(x * mul % 13)
        cnt += 1
    else:
        extra += int(S[i]) * mul % 13
        extra %= 13

    mul = mul * 10 % 13

# print(each_extras)

# print(extra)
dp = [[0 for i in range(13)] for j in range(cnt+1)]
dp[0][extra % 13] = 1
for i in range(cnt):
    for extras in each_extras[i]:
        for j in range(13):
            dp[i+1][(extras + j)%13] += dp[i][j]
            dp[i+1][(extras + j)%13] %= mod

# print(dp)
print(dp[-1][5] % mod)

"""
S = list(str(input()))

dp = [[0 for i in range(13)]for j in range(len(S)+1)]
dp[0][0] = 1
S.reverse()
mul = 1
for i in range(len(S)):
    if S[i] == "?":
        for j in range(10):
            for k in range(13):
                dp[i+1][(mul*j+k)%13] += dp[i][k]
                dp[i+1][(mul*j+k)%13] %= mod
    else:
        for k in range(13):
            dp[i+1][(int(S[i])*mul+k)%13] += dp[i][k]
            dp[i+1][(int(S[i])*mul+k)%13] %= mod
    mul *= 10
    mul %= 13

# print(dp)
print(dp[-1][5])
"""
