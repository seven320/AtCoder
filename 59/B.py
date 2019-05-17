# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

A = int(input())
B = int(input())

if A > B:
    print("GREATER")
elif A < B:
    print("LESS")
else:
    print("EQUAL") 
