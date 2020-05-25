# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, M, X = LI()
C = np.array([0 for i in range(N)])
A = np.array([[0 for i in range(M)] for j in range(N)])
for i in range(N):
    ca = LI()
    C[i] = ca[0]
    for j in range(M):
        A[i][j] = ca[1+j]


ans = mod
# 10進数のnをk進数のリストに変換
def n2kdigit(n,k):
    digits = []
    while n > 0:
        digits.append(n % k)
        n = n // k
    while len(digits) < N:
        digits.append(0)
    return digits

for i in range(2 ** N):
    skill = np.array([0 for i in range(M)])
    digit = np.array(n2kdigit(i, 2))
    for j in range(N):
        if digit[j]:
            skill += A[j]
    # print(skill)
    if np.all(skill >= X):
        ans = min(ans, sum(digit * C))
        # print(ans)

if ans == mod:
    print("-1")
else:
    print(ans)
    