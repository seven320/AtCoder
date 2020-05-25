# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, K = LI()
A = LI()

for i in range(len(A)):
    A[i] -= 1

next_city = 0
visited = [-1 for i in range(N)]
visited[0] = 0
for n in range(N):
    next_city = A[next_city]
    if visited[next_city] != -1:
        roop_s = visited[next_city]
        roop_cnt = n + 1 - roop_s
        break
    visited[next_city] = n + 1
ans = -1

if K - roop_s >= 0:
    amari = (K - roop_s) % roop_cnt
    next_city = 0
    for k in range(amari + roop_s):
        next_city = A[next_city]
    ans = next_city

else:
    next_city = 0
    for k in range(K):
        next_city = A[next_city]
    ans = next_city
# print(roop_s, roop_cnt)
print(ans + 1)