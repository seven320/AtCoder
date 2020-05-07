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

N, T = LI()
ab = []
for i in range(N):
    ab.append(LI())
ans = 0
time = 1
shops = [i for i in range(N)]
while T + 0.5 > time:
    cost = mod
    for i in shops:
        a,b = ab[i]
        if cost > a * time + b:
            r_shop = i
            cost = a * time + b
    if len(shops) > 0:
        shops.remove(r_shop)
    time += cost
    if T + 0.5 > time:
        ans += 1
    # move 
    time += 1

print(ans)