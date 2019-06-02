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

Graph = [[mod for i in range(N)] for i in range(N)]
for i in range(N):
    Graph[i][i] = 0

routes = []
for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    routes.append([a,b,c])
    Graph[a][b] = c
    Graph[b][a] = c

min_Graph = copy.deepcopy(Graph)
used = [[0 for i in range(N)] for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            min_Graph[i][j] = min(min_Graph[i][j],min_Graph[i][k]+min_Graph[k][j])

ans = 0
for i in range(M):
    a,b,c = routes[i]
    if min_Graph[a][b] == c:
        pass
    else:
        ans += 1

print(ans)
