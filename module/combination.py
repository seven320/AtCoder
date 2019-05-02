# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

#modに対応して高速なコンビネーションが求められる
# 階乗 & 逆元計算
factorial = [1]
inverse = [1]
for i in range(1, n+2):
    factorial.append(factorial[-1] * i % mod)
    inverse.append(pow(factorial[-1], mod-2, mod))

def combinations_count(n,r):
    if n-r < 0:
        return 0
    return factorial[n]*inverse[r]*inverse[n-r]%mod
