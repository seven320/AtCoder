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
N,M = LI()
ab = [[] for i in range(N)]
for i in range(N):
    ab[i] = LI()

hit_pos = []
for i in range(N):
    hit_pos.append(i+1-sum(ab[i]))

cnt = 0
hit_pos = set(hit_pos)
for i in hit_pos:
    if 1 <= i <= M:
        cnt += 1
print(cnt)
