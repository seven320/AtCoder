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

X, Y = LI()
ans = True
if Y % 2 == 1:
    ans = False

if X * 2 <= Y <= X * 4:
    pass
else:
    ans = False

if ans:
    print("Yes")
else:
    print("No")