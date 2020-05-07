# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7

#modに対応して高速なコンビネーションが求められる
# 階乗 & 逆元計算



d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

X,Y = LI()

if (X + Y) % 3 != 0:
    ans = 0
else:
    n = 10 ** 6
    factorial = [1]
    inverse = [1]
    for i in range(1, n+2):
        factorial.append(factorial[-1] * i % mod)
        inverse.append(pow(factorial[-1], mod-2, mod))

    def combinations_count(n,r):
        if n-r < 0:
            return 0
        return factorial[n]*inverse[r]*inverse[n-r]%mod
    m = int(X * 2 / 3 - Y / 3)
    n = int(Y * 2 / 3 - X / 3)
    if (X+Y) / 3 > X or (X + Y) / 3 > Y or m < 0 or n < 0:
        ans = 0
    else:
        ans = combinations_count((X + Y)//3, n)
print(ans)
