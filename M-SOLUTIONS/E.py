# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**6+3
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

Q = int(input())
xdn = [[] for i in range(Q)]
for i in range(Q):
    xdn[i] = [int(i) for i in input().split()]

for i in range(Q):
    ans = 1
    x,d,n = xdn[i]
    for j in range(n):
        ans = ans * (x + d * j) % mod
    print(ans)
