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

N = int(input())
wh = [[0,0] for i in range(N)]
max_w = -1
max_h = -1
for i in range(N):
    w,h = LI()
    wh[i] = [w,h]
    max_h = max(max_h,h)
    max_w = max(max_w,w)

dp = [[0 for i in range(max_h+2)] for j in range(max_w+2)]
box = {}
for h in range(max_h+2):
    for w in range(max_w+2):
        box[(h,w)] = 0

for i in range(N):
    w,h = wh[i]
    box[(h,w)] += 1

for part_sum in range(max_h+max_w+1):
    for h in range(part_sum+1):
        w = part_sum - h
        if 0 <= w < max_w and 0 <= h < max_h:
            dp[h+1][w+1] = max(dp[h][w] + box[(h+1,w+1)], dp[h][w+1], dp[h+1][w])

# print(dp)
print(max(max(dp[-2]),max(dp[:][-2])))
