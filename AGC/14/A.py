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

A, B, C = LI()

ans = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    a = A // 2
    b = B // 2
    c = C // 2
    A = (b + c)
    B = (a + c)
    C = (a + b)
    ans += 1
    if ans == 10000:
        break

if ans == 10000:
    print(-1)
else:
    print(ans)



