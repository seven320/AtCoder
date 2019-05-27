# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


r,D,x = map(int,input().split())
ans = [0 for i in range(11)]
ans[0] = x
for i in range(10):
    ans[i+1] = r*ans[i]-D

for i in range(1,11):
    print(ans[i])
