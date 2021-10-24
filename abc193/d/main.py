#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

K = int(input())
S = input()[:4]
T = input()[:4]

cnt = [K] * 10
for c in S:
    cnt[int(c)] -= 1
for c in T:
    cnt[int(c)] -= 1

def score(S):
    cnt = [0] * 10
    for c in S:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * (10 ** cnt[i])
    return ans 

ans = 0

for i in range(1, 10):
    if cnt[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or cnt[j] == 0:
            continue
        if score(S + str(i)) > score(T + str(j)):
            ans += cnt[i] * cnt[j]

for i in range(1, 10):
    if cnt[i]<2:
        continue
    if score(S + str(i)) > score(T + str(i)):
        ans += cnt[i] * (cnt[i] - 1)

N = 9*K - 8

print(ans / (N * (N - 1)))