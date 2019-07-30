# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
N = int(input())


def factorint(N):

    table = []
    while(N > 1):
        for i in range(2,N+1):
            if N%i == 0:
                while N%i == 0:
                    N = N//i
                    table.append(i)
                break
    return table

l = []
for n in range(1,N+1):
    l += factorint(n)
c = collections.Counter(l)
com = {74:0,24:0,14:0,4:0,2:0}
# print(c)
for key in c.keys():
    if c[key] >= 74:
        com[74] += 1
    if c[key] >= 24:
        com[24] += 1
    if c[key] >= 14:
        com[14] += 1
    if c[key] >= 4:
        com[4] += 1
    if c[key] >= 2:
        com[2] += 1
# print(com)
ans = 0
ans += com[74]
ans += com[24] * (com[2] - 1)
ans += com[14] * (com[4] - 1)
ans += com[4] * (com[4] - 1)* (com[2] - 2) //2
print(ans)
