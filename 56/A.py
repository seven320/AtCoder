# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

a,b = map(str,input().split())

if a == "H" and b == "H":
    tp = True
elif a=="D" and b == "H":
    tp = False
elif a=="D" and b=="D":
    tp = True
else:
    tp = False


if tp:
    print("H")
else:
    print("D")
