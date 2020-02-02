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

"""
nC3
|b - c| < a < |b + c|

nC2
b_i, c_iを除くiの中で|b-c|< a <b+cを満たすaの数をタス
"""

N = int(input())
L = LI()
L.sort()

ans = 0

combs = []
for i in range(N):
    for j in range(i+1, N):
        print([(i,j), abs(L[i] - L[j]), L[i] + L[j]])
        combs.append([(i,j), abs(L[i] - L[j]), L[i] + L[j]])

for comb in combs:
    tmp = 0
    ij, mi, ma = comb
    i,j = ij
    print(i,j)
    print(mi, ma)
    r = bisect.bisect_left(L, ma)
    l = bisect.bisect_right(L, mi)
    print("rl",r,l)
    tmp += r - l
    if l <= i <= r and tmp > 0:
        tmp -= 1
    if l <= j <= r and tmp > 0:
        tmp -= 1
    print(tmp)
    ans += tmp
print(ans)
