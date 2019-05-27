# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,M = map(int,input().split())

#cが多い
if 2*N < M:
    ans = N
    ans += (M - 2*N)//4
else:
#Sが多い
    ans = M//2
print(ans)
