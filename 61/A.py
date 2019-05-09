# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

A,B,C = map(int,input().split())

if C >= A and C <= B:
    print("Yes")
else:
    print("No")

    
