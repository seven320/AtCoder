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

X = int(input())

def solve(X):
    for a in range(1000):
        for b in range(-1000, 1000):
            a ** 5 - b ** 5
            if a ** 5 - b ** 5 == abs(X):
                return a, b

a,b = solve(X)
if a ** 5 - b** 5 == X:
    print(a, b)
else:
    print(b, a)