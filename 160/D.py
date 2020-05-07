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


N, X, Y = LI()
X -= 1
Y -= 1
anss = [0 for i in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        anss[min(
            abs(i - j), 
            abs(X - i) + 1 + abs(j - Y),
            abs(Y - i) + 1 + abs(X - j)
        )] += 1

for i in range(1, N):
    print(anss[i])
