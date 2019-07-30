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
ag,a_s,ab = [int(i) for i in input().split()]
bg,bs,bb = [int(i) for i in input().split()]

dp = [0 for i in range(N+1)]
g_v = bg - ag
s_v = bs - a_s
b_v = bb - ab
if g_v > 0:
    for i in range(ag,N+1):
        dp[i] = max(dp[i],dp[i-ag] + g_v)
if s_v > 0:
    for i in range(a_s,N+1):
        dp[i] = max(dp[i],dp[i-a_s] + s_v)
if b_v > 0:
    for i in range(ab,N+1):
        dp[i] = max(dp[i],dp[i-ab] + b_v)

N += max(dp)
dp = [0 for i in range(N+1)]
g_v = -bg + ag
s_v = -bs + a_s
b_v = -bb + ab
if g_v > 0:
    for i in range(bg,N+1):
        dp[i] = max(dp[i],dp[i-bg] + g_v)
if s_v > 0:
    for i in range(bs,N+1):
        dp[i] = max(dp[i],dp[i-bs] + s_v)
if b_v > 0:
    for i in range(bb,N+1):
        dp[i] = max(dp[i],dp[i-bb] + b_v)

N += max(dp)
print(N)
