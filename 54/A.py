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
if A==B:
    ans = "Draw"
else:
    if A == 1:
        ans = "Alice"
    elif B == 1:
        ans = "Bob"
    elif A>B:
        ans = "Alice"
    else:
        ans = "Bob"
print(ans)
