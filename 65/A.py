# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


X,A,B = map(int,input().split())

if B <= A:
    print("delicious")
else:
    if B <= A+X:
        print("safe")
    else:
        print("dangerous") 
