# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
coin = set()
for i in range(N):
    s = list(int(i) for i in input().split())
    s.sort()
    d = (s[0],s[1])
    if d not in coin:
        coin.add(d)

print(len(coin))
