# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

H,W = map(int,input().split())
C = [[] for i in range(H)]
for i in range(H):
    C[i] = [str(i) for i in input().split()]

for i in range(H):
    c = C[i]
    print("".join(c))
    print("".join(c))
