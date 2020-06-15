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

X, N = LI()
p = LI()

ans = mod
for i in range(100):
    if X - i not in p:
        ans = X - i
        break
    if X + i not in p:
        ans = X + i
        break

print(ans)
    