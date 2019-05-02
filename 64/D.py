# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N = int(input())
S = str(input())


l,r = 0,0
stack = 0
for i in range(N):
    if S[i]==")":
        if stack > 0:
            stack -= 1
            r -= 1
        else:
            l += 1
    else:
        r += 1
        stack += 1

print("("*l+S+")"*r)
