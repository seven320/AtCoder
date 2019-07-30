# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

H,W,N = map(int,input().split())
ab = [[] for i in range(N)]
for i in range(N):
    ab[i] = [int(i) for i in input().split()]

sum_table = []
