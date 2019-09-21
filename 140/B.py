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
A = LI()
B = LI()
C = LI()

ans = sum(B)
pre = -1
for a in A:
    if pre + 1 == a:
        ans += C[pre-1]
    pre = a

print(ans)
