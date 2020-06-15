#!/usr/bin/env python3
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

N = int(input())

def factorint(N):
    """
    Nを作っている素数を辞書で返す．
    input 100
    output Counter({2: 2, 5: 2})
    """
    table = []
    tmp = 2
    while(N > 1):
        for i in range(tmp,N+1):
            if N%i == 0:
                while N%i == 0:
                    N = N//i
                    table.append(i)
                tmp = i+1
                break
    table_ = collections.Counter(table)
    return table_

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

# factors = factorint(N)
factors = primes(N)
ans = 0
print(factors)
for key in factors.keys():
    f_c = factors[key]
    tmp = 1
    while f_c >= tmp:
        ans += 1
        f_c -= tmp
        tmp += 1

print(ans)