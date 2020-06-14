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

N, H = LI()
ab = [[]] * N
a = [0] * N
b = [0] * N

for i in range(N):
    a[i], b[i] = LI()
    ab[i] = [a[i], b[i]]

a_max = max(a)
ans = 0
b.sort(reverse= 1)
for i in range(N):
    if H <= 0:
        break
    if b[i] > a_max:
        H -= b[i]
        ans += 1
if H > 0:
    ans += math.ceil(H / a_max)
print(ans)
