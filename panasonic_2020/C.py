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

a,b,c = LI()
if c - a - b >= 0:
    if 4 * a* b < (c - a- b) ** 2:
        ans = 1
    else:
        ans = 0
else:
    ans = 0
if ans:
    print("Yes")
else:
    print("No")
