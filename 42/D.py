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


H,W,A,B = LI()

dp = [[0 for i in range(W+1)] for j in range(H+1)]

for i in range(W+1):
    dp[0][i] = 1
for i in range(H+1):
    dp[i][0] = 1


for xy in range(H+W):
    for x in range(xy+1):
        y = xy - x
        if x >= W or y >= H:
            pass
        else:
            print(x,y)
            if y+1 == B and x >= H -A:
                dp[x+1][y+1] = dp[x][y+1]
            elif x+1 == W:
                dp[x+1][y+1] = dp[x+1][y]
            elif y+1 == H:
                dp[x+1][y+1] = dp[x][y+1]
            else:
                dp[x+1][y+1] = dp[x][y+1] + dp[x+1][y]

print(dp)
print(dp[W-1][H-1])
