# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N = int(input())

s = N-8+1


for day in range(s,N+1):
    print(day)
