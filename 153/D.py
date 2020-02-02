# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

H = int(input())
"""
100
50 50
25 25 25 25
12 * 8
6 * 16
3 * 32
1 * 64
ans = 1 + 2 + 4 + 8 + 16 + 32 + 64
"""
x = 1
for i in range(41):
    x *= 2
    if H < x:
        k = i
        break

anss = [1]
for i in range(41):
    anss.append(anss[-1] * 2 + 1)
print(anss[k])
