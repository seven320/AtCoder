# encoding:utf-8
import bisect  # bisect_left　これで二部探索の大小検索が行える
import collections
import copy
import fractions  # 最小公倍数などはこっち
import math
import random
import sys

import numpy as np
import pandas as pd

import hoge

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, K = LI()
H = LI()

dp = [mod for i in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(min(K + 1, N - i)):
        # print(i, j)
        dp[i+j] = min(dp[i] + abs(H[i] - H[i + j]), dp[i+j])

print(dp[-1])
