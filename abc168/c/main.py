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

A, B, H, M = LI()

pi = math.pi
h_p = [A * math.cos(2 * pi * (H * 60 + M) / 720), A * math.sin(2 * pi * (H * 60 + M) / 720)]
m_p = [B * math.cos(2 * pi * M / 60), B * math.sin(2 * pi * M / 60)]

# print(h_p, m_p)
length = ((h_p[0] - m_p[0])**2 + (h_p[1] - m_p[1])**2)**0.5
print(length) 
