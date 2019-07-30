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

N, D = LI()
X = [[] for i in range(N)]
for i in range(N):
    X[i] = LI()

cnt = 0
for i in range(N):
    for j in range(i+1,N):
        l = 0
        for d in range(D):
            l += (X[i][d] - X[j][d]) ** 2
        if math.sqrt(l) % 1 == 0:
            cnt += 1

print(cnt)
