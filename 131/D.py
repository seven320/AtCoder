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
BA = [[] for i in range(N)]
for i in range(N):
    a,b = LI()
    BA[i] = (b,a)

BA.sort()

tmp  = 0
for i in range(N):
    b,a = BA[i]
    tmp += a
    if b - tmp < 0:
        print("No")
        break
else:
    print("Yes")
