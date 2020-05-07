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
X = LI()

ans = mod
for i in range(1, 101):
    tmp = 0
    for x in X:
        tmp += (x - i) ** 2
    ans = min(ans, tmp)
print(ans)