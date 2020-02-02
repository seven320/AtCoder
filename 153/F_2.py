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

N, D, A = LI()
xh = []

for i in range(N):
    xh.append(LI())
xh.sort()
X = []
for i in range(N):
    X.append(xh[i][0])

bomb = [0 for i in range(N)]
ans = 0
now_dm = 0
for i in range(N):
    x,H = xh[i]
    now_dm += bomb[i]
    if now_dm >= H:
        pass
    else:
        ans += math.ceil((H - now_dm)/A)
        dm = math.ceil((H-now_dm)/A) * A
        ind = bisect.bisect_right(X, x+2*D)
        if i + 1 < N:
            bomb[i+1] += dm
        if ind < N:
            bomb[ind] -= dm

print(ans)
