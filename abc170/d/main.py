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

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
A = LI()

A.sort()
table = [0 for i in range(10**6 + 1)] # 約数のテーブル

cc = collections.Counter(A)


cnt = 0
for a in A:
    if table[a] == 0:
        for i in range(10 ** 6):
            if a * i > 10 ** 6:
                break
            table[a * i] = 1
        if cc[a] == 1:
            cnt += 1


print(cnt)
    