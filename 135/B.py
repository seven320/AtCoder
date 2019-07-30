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

N = int(input())
p = LI()

p_sorted = sorted(p)

cnt = 0
for i in range(len(p)):
    if p[i] != p_sorted[i]:
        cnt += 1
if cnt ==2 or cnt == 0:
    print("YES")
else:
    print("NO")
