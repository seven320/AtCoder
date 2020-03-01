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

N,K = LI()

mod = 10**9+7

#modに対応して高速なコンビネーションが求められる

n = 2000

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


"""
N = 5 , K = 2

i = 1
bbrrr
rbbrr
rrbbr
rrrbb

i = 2
brbrr
6

(N - K + 1) C i * 

00|||

|||00
||00|
|00||
00|||

K - i = 0
i + 1

"""

for i in range(1, K+1):
    print(combinations_count(N - K + 1, i) * combinations_count(K- i + (i - 1), K -i) % mod)