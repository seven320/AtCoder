# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,X,Y = map(int,input().split())
A = [int(i) for i in input().split()]

A.sort(reverse=1)
for i in range(N):
    if i%2==0:
        X+= A[i]
    else:
        Y += A[i]

if X>Y:
    print("Takahashi")
elif X<Y:
    print("Aoki")
else:
    print("Draw")
