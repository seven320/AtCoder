# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

x = int(input())

cnt = (x // 11)*2

if x % 11 == 0:
    ans = cnt
elif x % 11 > 6:
    ans = cnt + 2
else:
    ans = cnt + 1

print(ans)
