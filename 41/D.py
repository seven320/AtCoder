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

N,M = LI()
xy = [[0,0] for i in range(M)]

dp = [0 for i in range(N)]
dp[0] = 1
b = [0 for i in range(N)]

for i in range(M):
    b[xy[i][1]-1 |= 1 << ]
