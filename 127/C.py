# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


N,M = map(int,input().split())
L,R = [0 for i in range(M)],[0 for i in range(M)]
for i in range(M):
    L[i],R[i] = map(int,input().split())

ans_max = -1
ans_min = mod
for i in range(M):
    ans_max = max(ans_max,L[i])
    ans_min = min(ans_min,R[i])

ans = max(ans_min-ans_max+1,0)
print(ans)
