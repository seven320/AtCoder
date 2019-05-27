# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,M = map(int,input().split())
A = [int(i) for i in input().split()]
change = [0 for i in range(M)]
for i in range(M):
    change[i] = [int(i) for i in input().split()]

D = []

# 数を交換できるというのを一つに表すのがミソ
change = sorted(change,key=lambda x:x[1],reverse=True)
for i in range(M):
    b,c = change[i]
    D += [c]*b
    if len(D) > N:
        break

A.sort()
tmp = sum(A)
for i in range(min(N,len(D))):
    diff = D[i] - A[i]
    if diff > 0:
        tmp += diff
    else:
        break
print(tmp)
