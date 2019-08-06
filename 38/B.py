# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

dis_1 = LI()
dis_2 = LI()
ans = 0
for i in range(2):
    if dis_1[i] in dis_2:
        ans = 1

if ans:
    print("YES")
else:
    print("NO")
