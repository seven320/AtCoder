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

S = str(input())

exams = [i*8 for i in range(125)]
c = collections.Counter(list(S))
ans = False
for e in exams:
    cnt = collections.Counter(str(e).zfill(3))
    if "0" in cnt.keys():
        continue

    for key in cnt.keys():
        if cnt[key] <= c[key]:
            pass
        else:
            break
    else:
        ans = True
        break
if int(S) in [8, 16, 61, 24,42, 32,23, 48,84, 56,65, 64,46, 72,27, 88, 96, 69]:
    ans = True

if ans:
    print("Yes")
else:
    print("No")
