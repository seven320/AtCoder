# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
from heapq import heappush, heappop

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N, M = LI()
ab = []
for i in range(M):
    a,b = LI()
    a -= 1
    b -= 1
    ab.append([a,b])

roots = [mod for i in range(N)]
roots[0] = 0

adj = [[] for _ in range(N)]
for i in range(M):
    a, b = ab[i]
    adj[a].append((b, 1))

roots = [[] for _ in range(N)]

INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        # seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
                roots[to].append(v)
            elif dist[v] + cost == dist[to]: # コストが等しい時も実行
                heappush(hq, (dist[to], to))
                roots[to].append(v)
    return dist

dist = dijkstra(0, N)

if dist[-1] == INF:
    print(-1)
    sys.exit()

root_anss = []
ways = [[N-1]]

for i in range(len(roots)):
    roots[i] = list(set(roots[i]))

while ways:
    way = ways.pop()
    p = way[-1]
    for to in roots[p]:
        if to == 0:
            root_anss.append(way + [0])
        else:
            ways.append(way + [to])

for i in range(len(root_anss)):
    root_anss[i].reverse()

root_anss.sort()
for p in root_anss[0]:
    print(p + 1, end = " ")