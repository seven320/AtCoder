# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


N,X = map(int,input().split())
L = [int(i) for i in input().split()]

cnt = 1
now = 0
for i in range(N):
    now += L[i]
    if now <= X:
        cnt += 1
    else:
        break

print(cnt)
