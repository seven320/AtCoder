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


N, Q = LI()
c = LI()
lr = []
for i in range(Q):
    l, r = LI()
    l -= 1
    r -= 1
    lr.append((l, r))



tmp_list = []
for q in range(Q):
    l,r = lr[q]

    print(len(set(c[l:r+1])))


# keys = set(c)

# dics = []
# dic = {}
# for key in keys:
#     dic[key] = 0

# for i in range(N):
#     dic[c[i]] += 1
#     dics.append(copy.deepcopy(dic))

# for i in range(Q):
#     l, r = lr[i]
#     ans = 0
#     if l > 0:
#         left_dic = dics[l - 1]
#         right_dic = dics[r]
#         for key in keys:
#             if right_dic[key] - left_dic[key] > 0:
#                 ans += 1
#         print(ans)
#     else:
#         left_dic = dics[l - 1]
#         right_dic = dics[r]
#         for key in keys:
#             if right_dic[key] > 0:
#                 ans += 1
#         print(ans)


