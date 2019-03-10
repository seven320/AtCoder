# encoding:utf-8
import copy
import numpy as np
import random

n,m,c = map(int,input().split())
B = [int(i) for i in input().split()]
A = []
for i in range(n):
    a = [int(i) for i in input().split()]
    A.append(a)

A = np.array(A)
B = np.array(B)

ans = 0

# print(np.dot(A[0],B))
for i in range(n):
    if np.dot(A[i],B)+c>0:
        ans += 1

print(ans)
