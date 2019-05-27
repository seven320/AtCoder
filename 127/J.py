# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
dp = [[0,0] for i in range(N)]
for i in range(N):
    a,b = map(int,input().split())
    if i == 0:
        dp[0] = [a,b]
    else:
        dp[i][0] = max(fractions.gcd(dp[i-1][0],a),fractions.gcd(dp[i-1][1],a))
        dp[i][1] = max(fractions.gcd(dp[i-1][0],b),fractions.gcd(dp[i-1][1],b))

print(max(dp[-1]))
