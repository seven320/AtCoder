# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7

def LI(): return list(map(int, sys.stdin.readline().split()))


N,M = LI()

ab = [i for i in range(M)]
c = [[] for i in range(M)]
for m in range(M):
    ab[m] = LI()
    c_tm = LI()
    for i in range(len(c_tm)):
        c_tm[i] -= 1
    c[m] = c_tm

dp = [mod for j in range(2**N)]

def digit2list(num):
    arr = [0 for i in range(M)]
    cnt = 0
    while num > 0:
        if num % 2 == 1:
            arr[cnt] = 1
        cnt += 1
        num //= 2
    return arr

for m in range(M):
    print(m)
    for i in range(2**len(c[m])):
        ons = digit2list(i)
        tmp = 0
        for i,on in enumerate(ons):
            if on:
                tmp += 2**c[m][i]
        print(ons)
        if dp[tmp] > ab[m][0]:
            dp[tmp] = ab[m][0]
            for j in range(2**N - tmp)
        

if dp[-1] == mod:
    print(-1)
else:
    print(dp[-1])

