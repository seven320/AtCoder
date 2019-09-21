# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import heapq

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
N,M = LI()
A = LI()

pq = []
for a in A:
    heapq.heappush(pq,-a)

for _ in range(M):
    heapq.heappush(pq,-(-heapq.heappop(pq) // 2))
    # print(pq)

print(-sum(pq))
