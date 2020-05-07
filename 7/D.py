# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))
A, B = LI()

def cnt_bans(x):
    x = list(map(int, list("{:020}".format(x))))
    dp = [[0, 0] for i in range(21)]
    dp[0][0] = 1
    for i in range(20):
        c = x[i]
        for j in [0, 1, 2, 3, 5, 6, 7, 8]:
            if j < c:
                dp[i + 1][1] += dp[i][1] + dp[i][0]
            elif j == c:
                dp[i + 1][0] += dp[i][0]
                dp[i + 1][1] += dp[i][1]
            else:
                dp[i + 1][1] += dp[i][1]
    return dp[-1][0] + dp[-1][1] - 1

print(B - A + 1 - (cnt_bans(B) - cnt_bans(A - 1)))