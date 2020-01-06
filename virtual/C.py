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

X,Y = LI()
dp = [[0 for i in range(Y+3)] for j in range(X+3)]

dp[1][2] = 1
dp[2][1] = 1

for ij in range((X+Y)//3 + 1):
    for i in range(ij, ij * 3 - ij):
        j = ij * 3 - i
        print(i,j)
        dp[i+2][j+1] += dp[i][j]
        dp[i+1][j+2] += dp[i][j]

print(dp)

print(dp[X][Y])
