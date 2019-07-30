# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

a,b,x = map(int,input().split())
ans = (b+1) // x - (a-1) // x
if (b+1) % x == 0:
    ans -= 1
# if (a-1) % x == 0:
#     ans -= 1
print(ans)
