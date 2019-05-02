# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N = int(input())
a = [int(i) for i in input().split()]

a.sort()
print(a[-1]-a[0])
