# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

a,b,x = LI()

water_area = x / a
if water_area >= (a * b / 2):
    b_ = (a * b - water_area) * 2 / a
    theta = math.degrees(math.atan(b_ / a))
else:
    a_ = (water_area * 2 / b)
    theta_ = math.degrees(math.atan(a_ / b))
    theta = 90 - theta_
print(theta)
