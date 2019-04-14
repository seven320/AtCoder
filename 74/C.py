# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

A,B,C,D,E,F = map(int,input().split())

water = []
for ai in range(int(F/(A*100))+1):
    for bi in range(int(F/(B*100))+1):
        if (ai*A+bi*B)*100>F:pass
        else:
            water.append((ai*A+bi*B)*100)

suger = []
for ci in range(int(F/C)+1):
    for di in range(int(F/D)+1):
        if ci*C+di*D > F:
            pass
        else:suger.append(ci*C+di*D)

water = list(set(water))
suger = list(set(suger))
water.remove(0)
pure = 0
ans_s,ans_w = 0,A*100
for wi in range(len(water)):
    for si in range(len(suger)):
        if water[wi]+suger[si]>F:pass
        else:
            if pure<suger[si]/(water[wi]+suger[si])<=(E/(100+E)):
                ans_s = suger[si]
                ans_w = water[wi]
                pure = suger[si]/(water[wi]+suger[si])

print(ans_s+ans_w,end="")
print(" ",end="")
print(ans_s)
