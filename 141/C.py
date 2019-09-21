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

N,K,Q = LI()
A = [0 for i in range(Q)]
for i in range(Q):
    A[i] = int(input()) - 1

cnt = {}

for i in range(N):
    cnt[i] = 0

for a in A:
    cnt[a] += 1

for i in range(N):
    if K - Q + cnt[i] > 0:
        print("Yes")
    else:
        print("No")
