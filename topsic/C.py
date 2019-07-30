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

r,c = LI()
C = [[0 for i in range(c)]for j in range(r)]

ans = True
for i in range(r):
    cnt = 0
    pre = ""
    for j in range(c):
        if C[i][j] == "*" and cnt == 0:
            left = j
            right = j
            cnt += 1
        elif C[i][j] == "*":
            cnt += 1
            right = j
