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
A = [int(i) for i in input().split()]

A_ = list(set(A))
if len(A_) % 2 == 1:
    ans = len(A_)
else:
    ans = max(1,len(A_)-1)

print(ans)
"""

"""
