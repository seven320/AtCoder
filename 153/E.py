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

H, N = LI()
ab = []
for i in range(N):
    ab.append(LI())

dp = [[mod for i in range(H + 2)] for i in range(N + 2)]
for i in range(N):
    dp[i][0] = 0

for n in range(N):
    A,B = ab[n]
    for h in range(H + 2):
        dp[n + 1][h] = min(dp[n][h], dp[n + 1][max(0, h - A)] + B)
# print(dp)
print(dp[-2][H])
