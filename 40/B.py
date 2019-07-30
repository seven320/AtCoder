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

n = int(input())

ans = mod
for i in range(1,math.floor(math.sqrt(n))+1):
    edge = n//i
    extra = n - edge * i
    ans = min(ans, abs(edge-i) + extra)

print(ans)
