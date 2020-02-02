# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
import heapq

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, M = LI()
ab = []
for i in range(N):
    ab.append(LI())

ab.sort()
candidates = []

ans = 0
s = 0
for i in range(1, M+ 1):
    for j in range(s, N):
        a,b = ab[j]
        if a <= i:
            heapq.heappush(candidates, -b)
        else:
            s = j
            break
    else:
        s = j + 1
    if len(candidates) > 0:
        # print(candidates)
        ans += -1 * heapq.heappop(candidates)

print(ans)
"""
4 3 2

3 2 3 1
2 3 1


"""
