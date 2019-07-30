# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
a = LI()


dp = [0 for i in range(N)]

dp[1] = abs(a[1]-a[0])

for i in range(N-2):
    dp[i+2] = min(dp[i]+abs(a[i+2]-a[i]),dp[i+1]+abs(a[i+2]-a[i+1]))

# print(dp)
print(dp[-1])
