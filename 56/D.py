# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,K = map(int,input().split())
a = [int(i) for i in input().split()]

a.sort()
ans = N

psum = 0
for i in range(N-1,-1,-1):
    if psum+a
