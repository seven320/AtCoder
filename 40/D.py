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
aby = [[] for i in range(M)]
for i in range(M):
    aby[i] = LI()
Q = int(input())
vw = [[] for i in range(Q)]
for i in range(Q):
    vw[i] = LI()

loads = {}
for i in range(M):
    loads[i] = []
for i in range(M):
    a,b,y = aby[i]
    a -= 1
    b -= 1
    loads[a].append((b,y))
    loads[b].append((a,y))

for i in range(Q):
    v,w = vw[i]
    v -= 1
    v = [v]
    used = []
    while len(v) > 0:
        now = v.pop()
        used.append(now)
        for load in loads[now]:
            city,y = load
            if y > w:
                if city in used:
                    pass
                else:
                    v.append(city)
    print(len(set(used)))
