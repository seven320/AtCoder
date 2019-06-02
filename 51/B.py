# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

K,S = map(int,input().split())

ans = 0
for i in range(K+1):
    for j in range(K+1):
        if K >= S-i-j >= 0:
            ans += 1
print(ans)
