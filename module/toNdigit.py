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



# 10進数のnを2進数のリストに変換
def n2kdigit(n,k):
    digits = []
    while n > 0:
        digits.append(n % k)
        n = n // k

    return digits

#2進数のリストを10進数のnに変換
def kdigit2n(digits,k):
    n = 0
    for i, digit in enumerate(digits):
        n += digit * k ** i

    return n

print(nto_kdigit(4, k = 2))
