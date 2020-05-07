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

A = []
for i in range(3):
    A.append(LI())
N = int(input())
b = []
for i in range(N):
    b.append(int(input()))

tables = [[0,0,0] for i in range(3)]
for n in range(N):
    for i in range(3):
        for j in range(3):
            if A[i][j] == b[n]:
                tables[i][j] = 1

ans = 0
for i in range(3):
    if tables[i][0] == tables[i][1] == tables[i][2] == 1:
        ans = 1
    if tables[0][i] == tables[1][i] == tables[2][i] == 1:
        ans = 1
    if tables[0][0] == tables[1][1] == tables[2][2] == 1:
        ans = 1
    if tables[0][2] == tables[1][1] == tables[2][0] == 1:
        ans = 1

if ans:
    print("Yes")
else:
    print("No")
