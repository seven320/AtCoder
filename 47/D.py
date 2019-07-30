# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,T = map(int,input().split())
A = [int(i) for i in input().split()]

L_min = [mod for i in range(N)]
L_min[0] = A[0]
for i in range(1,N):
    L_min[i] = min(L_min[i-1],A[i])

A.reverse()
R_max = [0 for i in range(N)]
R_max[0] = A[0]
for i in range(1,N):
    R_max[i] = max(R_max[i-1],A[i])

R_max.reverse()

ans = 0
dif = -mod

for i in range(1,N):
    if dif < R_max[i] - L_min[i] and 0 < R_max[i] - L_min[i]:
        dif = R_max[i] - L_min[i]
        r,l = R_max[i],L_min[i]
        # print(dif)
        ans = 1
    elif dif == R_max[i] - L_min[i]:
        if r == R_max[i]:
            pass
        else:
            r,l = R_max[i],L_min[i]
            ans += 1

print(ans)
