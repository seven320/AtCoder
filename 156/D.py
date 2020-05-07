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

n, a, b = LI()

ans = pow(2, n, mod) - 1

def comb_mod(n, k, mod):
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod

    return (numerator * pow(denominator, mod - 2, mod)) % mod

ans -= comb_mod(n, a, mod)
ans -= comb_mod(n, b, mod)
print(ans)