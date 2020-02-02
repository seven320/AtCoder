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
ps = [0 for i in range(M)]
for i in range(M):
    p,s = input().split()
    p = int(p)
    p -= 1
    s = str(s)
    ps[i] = [p,s]

# ACs = [0 for i in range(N)]
tmp = 0
ans = [[0,0] for i in range(N)] # AC, WA
for i in range(M):
    p, s = ps[i]
    if ans[p][0]:
        pass
    else:
        if s == "AC":
            ans[p][0] = 1
        else:
            ans[p][1] += 1

anss = [0, 0]
for i in range(N):
    if ans[i][0]:
        anss[0] += 1
        anss[1] += ans[i][1]

print(anss[0], anss[1])
