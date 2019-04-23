# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

N = int(input())

A = []
for i in range(N):
    a = [int(i) for i in input().split()]
    A.append(a)

exist = True
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[j][k]>A[j][i]+A[i][k]:
                exist = False

if exist:
    for j in range(N):
        for k in range(N):
            tmp = 10**10
            for i in range(N):
                if j==i or i==k:
                    pass
                else:
                    tmp = min(tmp,A[j][i]+A[i][k])
            if A[j][k] < tmp:
                ans += A[j][k]
    ans = ans//2


print(ans)
