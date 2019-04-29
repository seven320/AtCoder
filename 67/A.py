# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

A,B = map(int,input().split())
if A%3==0 or B%3==0 or (A+B)%3==0:
    print("Possible")
else:
    print("Impossible")

    
