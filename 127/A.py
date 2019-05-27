# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

A,B = map(int,input().split())

if A >= 13:
    ans = B
elif A >= 6:
    ans = B//2
else:
    ans = 0
print(ans)
