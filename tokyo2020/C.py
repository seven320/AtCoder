# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

import numpy as np
mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, K = LI()
A = LI()

"""
明るさが一定値を超えると計算しなくて良い
一定？d > math.floort(N/2)
"""
if K > 30:
    b = [str(N)] * N
    print(" ".join(b))
    sys.exit()

lamps = [[0 for i in range(N)] for j in range(K + 1)]
lamps[0] = A

lamps = np.array(lamps)
"""
累積和〜
"""
# for i in range(K):
#     if lamps[i] == [N for i in range(N)]:
#         ans = [str(N) for i in range(N)]
#         print(" ".join(ans))
#     tmps = [0 for i in range(N)]
#     for j in range(N):
#         w = lamps[i][j]
#         tmps[max(0, j - w)] += 1
#         r = min(N-1, j + w)
#         if r + 1 < N:
#             tmps[r + 1] -= 1
#     hoge = 0
#     for j in range(N):
#         hoge += tmps[j]
#         lamps[i + 1][j] = hoge
for i in range(K):
    if lamps[i][-1] == N:
        if np.all(lamps[i] == np.ones(N) * N):
            ans = [str(N)] * N
            print(" ".join(ans))
            sys.exit()
    for j in range(N):
        tmp = lamps[i][j]
        if tmp == 0:
            lamps[i+1][j] += 1
        else:
            lamps[i + 1][max(0, j - tmp):min(N + 1, j + tmp) + 1] += 1
ans = lamps[-1].tolist()
ans = map(str, ans)
print(" ".join(ans))
# ans = lamps[-1]
# ans = map(str, ans)
# print(" ".join(ans))
