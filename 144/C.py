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


N = int(input())
ans = 10 ** 12
for i in range(1, math.ceil(N**0.5)+1):
    if N / i == N // i:
        # print(i, N // i)
        ans = min(ans, i + N // i - 2)
print(ans)
