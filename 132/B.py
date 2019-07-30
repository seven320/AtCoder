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
p = LI()
cnt = 0

for i in range(1,n-1):
    if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
        cnt += 1

print(cnt)
