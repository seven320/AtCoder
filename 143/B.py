# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
d = LI()
takoyakis = sum(d)
ans = 0
for takoyaki in d:
    ans += (takoyakis - takoyaki) * takoyaki
print(ans // 2)
