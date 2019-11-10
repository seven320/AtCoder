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
N, M = LI()
lrc = [[] for i in range(M)]
for m in range(M):
    L,R,c = LI()
    L -= 1
    R -= 1
    lrc[m] = [L,R,c]

# print(dp)
dp2 = [mod for i in range(N)]
dp2[0] = 0
for i in range(N):
    for j in range(i):
        dp2[i] = min(dp2[i], dp2[j] + dp[j][i])
if dp2[-1] == mod:
    print(-1)
else:
    print(dp2[-1])
