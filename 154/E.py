# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
K = str(input())

dp0 =[[0 for i in range(K+1)] for j in range(101)]
dp1 = [[0 for i in range(K+1)] for j in range(101)]

for i in range(101):
    for num in (0,1,2,3,4,5,6,7,8,9):
        if N[i] > num: # dp0
            for j in range(K+1):
                if num == 0:
                    dp0[i + 1][k + 1] += dp0[i][k]
                else:
                    dp0[i + 1][k] += dp0[i][k]
        else: # dp1
            for j in range(K+1):
                if num == 0:
                    dp1[i + 1]


    for j in range(K+1):

