# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

X,Y = map(int,input().split())

if abs(X-Y) > 1:
    print("Alice")
else:
    print("Brown")
