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
A,B = [0 for i in range(N)],[0 for i in range(N)]

for i in range(N):
    A[i],B[i] = map(int,input().split())

for i in range(N):
    if abs(A[i]-B[i]) == 0:
        print(-1)
    else:
        print(abs(A[i]-B[i]))
