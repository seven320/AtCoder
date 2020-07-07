#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
def f(n):
    if n < 2:
        return 1
    else:
        return n * f(n - 2)

"""
2,5が大事
11 > 9 > 7 > 5 > 3 > 1

10 > 8 > 6 > 4 > 2 > 1
10の個数

というより5の倍数をどう数えるかが重要．
まず10でぜんたいを割って10による部分をansにたす．
その後，5の倍数を取り出す．
"""
if N % 2 == 1:
    print("0")
    sys.exit()

# base_ans = 0
# fn = str(f(N))
# while True:
#     if len(fn) < 1:
#         break
#     if fn[-1] == "0":
#         base_ans += 1
#         fn = fn[:-1]
#     else:
#         break
# print(base_ans)

ans = 0
if N >= 10:
    N //= 10
    ans += N

n = copy.deepcopy(N)
while n > 4:
    n //= 5
    ans += n

print(ans)