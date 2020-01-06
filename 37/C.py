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

N,K = LI()
a = LI()

ans = 0
for n in range(N):
    ans += a[n] * min(N-K+1, n+1, N-n, K)
    # print(min(N-K+1, n+1, N-n, K))
print(ans)
