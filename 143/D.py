# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

"""
nC3
|b - c| < a < |b + c|

nC2
b_i, c_iを除くiの中で|b-c|< a <b+cを満たすaの数をタス
"""

N = int(input())
L = LI()
L.sort()

ans = 0
for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        ans += j - bisect.bisect_right(L[:j], L[i] - L[j])
print(ans)