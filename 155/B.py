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

ans = 1
for a in A:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            ans = 0


if ans:
    print("APPROVED")
else:
    print("DENIED")