# encoding:utf-8
import copy
import numpy as np
import random

n = int(input())
X = []
U = []
for i in range(n):
    x,u = map(str,input().split())

    X.append(float(x))
    U.append(u)

ans = 0
for i in range(n):
    if U[i]=="JPY":
        ans += X[i]
    else:
        ans += X[i]*380000

print(ans)
