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
s = len(str(N))
ans = 0
if s % 2 == 1:
    ans += (N - 10**(s-1)) + 1

for i in range(1,s,2):
    ans += 10**(i-1) * 9

print(ans)
