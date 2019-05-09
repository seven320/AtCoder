# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,M = map(int,input().split())
ways = []
for i in range(M):
    way = [int(i) for i in input().split()]
    ways.append(way)

ways.sort()
dp = [None for i in range(N+1)]

dp[1] = 0
cnt_way = 0
for j in range(N+1):
    for i in range(M):
        a,b,c = ways[i]
        if dp[a] != None:
            if dp[b] == None:
                dp[b] = dp[a] + c
            else:
                dp[b] = max(dp[b],dp[a]+c)

    if j == N-1:
        ans = dp[-1]

if ans == dp[-1]:
    pass
elif ans < dp[-1]:
    ans = "inf"

print(ans)
