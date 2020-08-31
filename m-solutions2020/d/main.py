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

# N = int(input())
# A = LI()

# tmp = 1000
# stocks = 0
# for i in range(N - 1):
#     if A[i] < A[i + 1]: # 明日の方が高い　買う
#         new_stocks = tmp // A[i]
#         stocks += new_stocks
#         tmp -= new_stocks * A[i]
#     else:# 明日の方が安い　うる
#         tmp += stocks * A[i]
#         stocks = 0
# tmp += stocks * A[-1]
# print(tmp)

N = int(input())
A = LI()

cash = 1000
stocks = 0
for i in range(N - 1): 
    if A[i] < A[i + 1]: # 明日の方が高いなら買えるだけ買い
        buy_stocks = cash // A[i]
        stocks += buy_stocks
        cash -= buy_stocks * A[i]
    else: # 値段が同じor安いなら全ての株を現金化しておく
        cash += stocks * A[i]
        stocks = 0
cash += stocks * A[-1] # 最終日には全てを現金化する
print(cash)

