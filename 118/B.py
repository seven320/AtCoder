# encoding:utf-8
import copy
import numpy as np
import random# TEMP:

"""
n,m = map(int,input().split())
ka = []
for i in range(n):
    ka.append([int(i) for i in input().split()])


ranking = [0 for i in range(m+1)]
print(ranking)
for i in range(n):
    for j in range(1,ka[i][0]+1):
        # print(ka[i][j])
        ranking[ka[i][j]]+=1

ans = 0

print(ans)
"""
# ans2

n,m = map(int,input().split())
res = set(range(1,m+1))
for i in range(n):
    k,*a = map(int,input().split())
    res &= set(a)
    # print(res)

print(len(res))
