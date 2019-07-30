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

N = int(input())
A = [0 for i in range(N)]
for i in range(N):
    A[i] = int(input())

A_c = copy.deepcopy(A)
A_c.sort()
for i in range(N):
    if A_c[-1] == A[i]:
        print(A_c[-2])
    else:
        print(A_c[-1])
