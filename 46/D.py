# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

s = str(input())
g,p = 0,0
ans = 0
for i in range(len(s)):
    if s[i] == "g":
        if g > p:
            ans += 1
            p += 1
        else:
            g += 1
    else:
        if g > p:
            p += 1
        else:
            ans -= 1
            g += 1

print(ans)
