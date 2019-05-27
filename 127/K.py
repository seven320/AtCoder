# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
ab = [[] for i in range(N)]
for i in range(N):
    ab[i] = map(int,input().split())

all = []
for i in range(N):
    all += ab[i]
count = collections.Counter(all)
ans = 0
delete = 0
for key in count.keys():
    ans += 1
    if count[key] == 1:
        a = all.index(key)
        if a % 2 == 1:
            if count[all[a-1]] == 1:
                delete += 1
        else:
            if count[all[a+1]] == 1:
                delete += 1

print(ans-delete//2)

"""
a b
b b
c d
"""
