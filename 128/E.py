# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,Q  = map(int,input().split())
stx = [[] for i in range(N)]
for i in range(N):
    stx[i] = list(map(int,input().split()))

stx = sorted(stx,key=lambda x:x[2])

D = [0 for i in range(Q)]
for i in range(Q):
    D[i] = int(input())

ans = [-1 for i in range(Q)]
for i in range(N):
    s,t,x = stx[i]
    for j in range(Q):
        if ans[j] == -1:
            if s-x <= D[j] < t-x:
                # print("input",D[j])
                ans[j] = x
        else:
            pass
for i in range(Q):
    print(ans[i])
