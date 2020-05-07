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

A = LI()

A_ii = copy.deepcopy(A)
for i in range(N):
    A_ii[i] += i
dic_A_ii = collections.Counter(A_ii)

A_jj = copy.deepcopy(A)

for j in range(N):
    A_jj[j] = -1 * A_jj[j] + j

ans = 0
dic_A_jj = collections.Counter(A_jj)
# print(dic_A_ii)
# print(dic_A_jj)

for ii_key in dic_A_ii.keys():
    ans += dic_A_jj[ii_key] * dic_A_ii[ii_key]

print(ans)