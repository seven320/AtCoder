# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


N = int(input())
T = [int(i) for i in input().split()]
M = int(input()) # juice
PM = [[] for i in range(M)]
for i in range(M):
    PM[i] = [int(i) for i in input().split()]

solve_time = sum(T)
for i in range(M):
    p,m = PM[i]
    print(solve_time-T[p-1]+m)
