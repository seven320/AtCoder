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

S = str(input())
ans = True
for i,s in enumerate(S):
    if i % 2 == 0 and s == "L" or i % 2 == 1 and s == "R":
        ans = False

if ans:
    print("Yes")
else:
    print("No")
