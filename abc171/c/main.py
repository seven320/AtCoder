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

index = []
while N > 0:
    N -= 1
    digit = N % 26
    index.append(digit)

    N -= digit
    N //= 26



ans = []
change = list("abcdefghijklmnopqrstuvwxyz")

# print(index)
index.reverse()


for i in range(len(index)):
    ans.append(change[index[i]])


print("".join(ans))


