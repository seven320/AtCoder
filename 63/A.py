# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


A,B = map(int,input().split())


if A+B >= 10:
    print("error")
else:
    print(A+B)
