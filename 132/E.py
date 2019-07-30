# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import numpy as np
from collections import deque # queue をつかうなら q = deque()


mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
N,M = LI()

um = [[] for i in range(M)]
for i in range(M):
    um[i] = LI()

S,T = LI()
S -= 1
T -= 1
routes = [[] for i in range(N)]

for i in range(M):
    u,m = um[i]
    u -= 1
    m -= 1
    routes[u].append(m)

used = [[mod,mod,mod] for i in range(N)]



# q = queue.Queue()
q = deque()
q.append((S,0))
# Deep First Serch
while q:
    now, cost = q.popleft()
    state = cost % 3
    if used[now][state] == mod:
        used[now][state] = cost
        for route in routes[now]:
            q.append((route,cost+1))

try:
    ans = used[T][0]
    if ans == mod:
        ans = -1
    else:
        ans = ans/3
except:
    ans = -1
print(int(ans))
