#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
A = LI()

"""
pairwise coprime 1,3,7,10
setwise coprime 2,3,4,10


coprimeかどうかで全部やる
"""

def primes(n): #試し割り法で各素因数とその指数を求める
    cnt=collections.defaultdict(int)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            while n%i==0:
                cnt[i]+=1
                n//=i
    if n!=1:
        cnt[n]+=1
    return cnt


def solve():
    gcd = A[0]
    for a in A:
        gcd = math.gcd(gcd, a)
    if gcd != 1:
        return "not coprime"

    history = {}
    for i in range(10**6):
        history[i] = 0

    for a in A:
        d = primes(a)
        for key in d.keys():
            history[key] += 1
            if history[key] > 1:
                return "setwise coprime"
    return "pairwise coprime"
 
    
print(solve())