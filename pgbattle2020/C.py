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

N = int(input())
A = LI()

position = {}
for i in range(1, N+1):
    position[i] = []

for i, a in enumerate(A):
    position[a].append(i)
# print(position)

diff = [0 for i in range(2*N - 1)]
for key in position.keys():
    # print(position[key])
    l, r = position[key]
    diff[abs(l - r)] += 1

ans = 0
for i in range(1, 2*N-1):
    ans += diff[i]
    print(ans)

print(ans)
