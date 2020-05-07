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

K, N = LI()
A = LI()

ans = mod
diff = [0 for i in range(N)]
for i in range(N - 1):
    diff[i] = A[i + 1] - A[i]
diff[-1] = (K - A[-1]) + A[0]
# print(diff)
ans = K - max(diff)
print(ans)