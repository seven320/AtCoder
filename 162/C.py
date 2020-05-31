# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
# import math
import sys
import collections

from math import gcd
mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

K = int(input())
# """answer 1
ans = 0
tmp = {}
for i in range(201):
    tmp[i] = 0

for i in range(1, K +1):
    for j in range(1, K +1):
        tmp[gcd(i, j)] += 1

for k in range(1, K +1):
    for key in tmp.keys():
        ans += gcd(key, k) * tmp[key]
print(ans)
# ""


"""answer 2　ぎりぎり
ans = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K +1):
            ans += gcd(gcd(i,j), k)
print(ans)

"""
"""超賢い回答
ans = 0

# (1,2,3)
for i in range(1, K +1):
    for j in range(i+ 1, K + 1):
        for k in range(j + 1, K + 1):
            ans += gcd(gcd(i, j), k) * 6

# (1,2,2)
for i in range(1, K + 1):
    for j in range(i+ 1, K+1):
        ans += gcd(i, j) * 3 * 2

# (1,1,1)
for i in range(1, K +1):
    ans += i
print(ans)

"""