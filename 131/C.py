# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

# 最小公倍数
def lcm(x,y):
    return (x*y)//fractions.gcd(x,y)

def LI(): return list(map(int, sys.stdin.readline().split()))

A,B,C,D = LI()
A -= 1
upper_cnt = B - (B // C + B // D - B //lcm(D,C))
lower_cnt = A - (A // C + A // D - A //lcm(C,D))


print(upper_cnt-lower_cnt)
