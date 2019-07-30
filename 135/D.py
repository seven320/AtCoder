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
each_extras = [[0 for i in range(10)] for i in range(S.count("?"))]
cnt = 0
for i in range(len(S)):
    if S[i] != "?":
        extra += int(S[i]) * 10 ** i
    else:
        each_extras[cnt] = [0 for i in range(13)]
        for x in range(10):
            each_extras[cnt][x * 10 ** i % 13] = 1
        cnt += 1

# print(extra)
dp = [[0 for i in range(13)] for j in range(cnt+1)]
dp[0][extra % 13] = 1
for i in range(cnt):
    for j in range(13):
        for e_i in range(13):
            if each_extras[i][e_i]:
                dp[i+1][(j+e_i) % 13] += dp[i][j]
    for j in range(13):
        dp[i+1][j] = dp[i+1][j] % mod

# print(dp)
print(dp[-1][5] % mod)
