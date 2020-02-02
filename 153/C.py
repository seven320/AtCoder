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

N, K = LI()
H = LI()
H.sort()
ans = 0
if K >= len(H):
    print(0)
    sys.exit()

if K == 0:
    print(sum(H))
else:
    print(sum(H[:-K]))
