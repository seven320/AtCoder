# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,K,L = map(int,input().split())
pq = [[] for i in range(K)]
for i in range(K):
    pq[i] = [int(i) for i in input().split()]

rs = [[] for i in range(L)]
for i in range(L):
    rs[i] = [int(i) for i in input().split()]

loads = [[] for i in range(N)]
for i in range(K):
    p,q = pq[i]
    p -= 1
    q -= 1
    loads[p] += [q]
    loads[q] += [p]

train = [[] for i in range(N)]
for i in range(L):
    r,s = rs[i]
    r -= 1
    s -= 1
    train[r] += [s]
    train[s] += [r]
