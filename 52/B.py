# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


N = int(input())
S = str(input())

x = 0
ans = 0
for i in range(N):
    if S[i] == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans,x)
print(ans)
