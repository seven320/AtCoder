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

all = (10 **N) % mod
no_zero = (9**N) % mod
no_nine = (9**N) 
no_zero_nine = 8 ** N

A = 1
no_zero = 1
no_nine = 1
no_zero_nine = 1

for i in range(N):
    A = A * 10 % mod
    no_zero = no_zero * 9 % mod
    no_zero_nine = no_zero_nine * 8 % mod

ans = (A - (no_zero * 2 - no_zero_nine)) % mod
    

print(ans)
