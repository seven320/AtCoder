# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


a,b,c = map(int,input().split())
if a+b == c or a == b+c or b == a+c:
    print("Yes")
else:
    print("No")
