# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
base = 2019


L,R = LI()
l = L % base
r = R % base
if (L // base + 1) * base <= R:
    ans = 0
    # print("hoge")
elif l >= r:
    ans = 0
else:
    ans = mod
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            ans = min(ans,i * j % base)
print(ans)
