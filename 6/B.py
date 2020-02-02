# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
mod = 10007
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

n = int(input())
a = [0 for i in range(max(n, 3))]
a[2] = 1
if n > 3:   
    for i in range(3, n):
        a[i] = (a[i-1] + a[i-2] + a[i-3])%mod

print(a[n-1])

