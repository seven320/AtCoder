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
c
S = str(input())

if S[:14] == "WBWBWWBWBWBWWB":
    print("Do")
elif S[:14] == "WBWWBWBWBWWBWB":
    print("Re")
elif S[:14] == "WWBWBWBWWBWBWW":
    print("Mi")
elif S[:14] == "WBWBWBWWBWBWWB":
    print("Fa")
elif S[:14] == "WBWBWWBWBWWBWB":
    print("So")
elif S[:14] == "WBWWBWBWWBWBWB":
    print("La")
else:
    print("Si")