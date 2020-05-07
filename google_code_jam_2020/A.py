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

def solve(X, Y, M):
    for i, m in enumerate(M):
        if m == "N":
            Y += 1
        elif m == "W":
            X -= 1
        elif m == "S":
            Y -= 1
        elif m == "E":
            X += 1
        else:
            print("input error")

        if abs(X) + abs(Y) <= i + 1:
            return i + 1
    return "IMPOSSIBLE"

T = int(input())

anss = []
for t in range(T):
    X, Y, M = input().split()
    anss.append(solve(int(X), int(Y), str(M)))

for i, ans in enumerate(anss):
    print("Case #{}: {}".format(i + 1, ans))




