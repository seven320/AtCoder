import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える

x,y,z,k = map(int,input().split())
A = [i for i in map(int,input().split())]
B = [i for i in map(int,input().split())]
C =[i for i in map(int,input().split())]

ab = []
for i in A:
    for j in B:
        ab.append(i+j)

ab.sort()
ab.reverse()
if len(ab)>k:
    ab_sel = ab[0:k]
else:
    ab_sel = ab

anss = []
for i in ab_sel:
    for j in C:
        anss.append(i+j)


anss.sort()
anss.reverse()

for i in range(k):
    print(anss[i])
