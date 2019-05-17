# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

A,B,C = map(str,input().split())

if A[-1] == B[0] and B[-1] == C[0]:
    print("YES")
else:
    print("NO")
