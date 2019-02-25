# encoding:utf-8
import copy
import numpy as np
import random

n = int(input())
A = []
for i in range(2):
    A.append([int(i) for i in input().split()])

B =[[0 for i in range(n)] for j in range(2)]
B[0][0] = A[0][0]
for i in range(1,n):
    B[0][i] = B[0][i-1]+A[0][i]

B[1][0]=A[0][0]+A[1][0]
for i in range(1,n):
    B[1][i] = max(B[1][i-1],B[0][i])+A[1][i]

# print(B)

ans = B[-1][-1]

print(ans)
