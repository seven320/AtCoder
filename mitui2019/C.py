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
X = int(input())
prices = [100,101,102,103,104,105]

#
# dp = [0 for i in range(2002)]
# for price in prices:
#     dp[price] = 1
# for i in range(len(dp)):
#     for price in prices:
#         if i > price and dp[i-price] == 1:
#             dp[i] = 1
#
# if X > 2000:
#     print("1")
# else:
#     print(dp[X])



dp = [0 for i in range(max(X + 1, 106))]
for price in prices:
    dp[price] = 1
for i in range(len(dp)):
    for price in prices:
        if i > price and dp[i - price] == 1:
            dp[i] = 1

print(dp[X])
