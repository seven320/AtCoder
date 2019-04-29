# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


n = int(input())
a = [int(i) for i in input().split()]

dp = [[0 for i in range(n+1)] for j in range(n+1)]

count = [0 for i in range(n+1)]


used = []
cnt =0
for i in range(n+1):
    if not a[i] in used:
        cnt += 1
        used.append(a[i])

    count[i] = cnt

dp[0] = count
for i in range(n+1):
    dp[i][i] = 1

for j in range(1,n+1):
    for i in range(1,j):
        dp[i][j] = (dp[i-1][j-1]+dp[i][j-1])%(10**9+7)


for i in range(n+1):
    print(dp[i][-1])
