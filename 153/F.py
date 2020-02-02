# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

import collections

dms = collections.deque()
mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N, D, A = LI()
xh = []
for i in range(N):
    xh.append(LI())
xh.sort()

# sum_dm = [] # start + 2 * D
ans = 0
sum_dm = 0
for i in range(N):
    X, H = xh[i]
    while len(dms) > 0:
        if dms[0][0] + 2 * D < X:
            x, dm = dms.popleft()
            sum_dm -= dm
        else:
            break
    H -= sum_dm
    if H > 0:
        ans += math.ceil(H / A)
        dms.append([X, math.ceil(H/A) * A])
        sum_dm += math.ceil(H/A) * A
print(ans)
