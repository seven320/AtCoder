# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
from decimal import Decimal

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
TA = [[] for i in range(N)]
for i in range(N):
    TA[i] = [int(i) for i in input().split()]

min_T,min_A = 1,1
for i in range(N):
    t,a = TA[i]
    # if min_T >= t or min_A>= a:
    multi = max(math.ceil(Decimal(min_T) / Decimal(t)),math.ceil(Decimal(min_A)/Decimal(a)),1)
    min_T,min_A = t*multi, a*multi

print(min_A+min_T)
