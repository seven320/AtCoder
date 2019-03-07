# encoding:utf-8
import copy
import numpy as np
import random

c = []
for i in range(3):
    tem = [int(i) for i in input().split()]
    c.append(tem)

a = [0 for i in range(3)]
b = [0 for i in range(3)]
for i in range(3):
    min_line =  min(c[i])
    for j in range(3):
        c[i][j] -= min_line
    # a[i] += min_line

# print(c)

c = np.array(c)

for i in range(3):
    min_row = min(c[:,i])
    for j in range(3):
        c[j,i] -= min_row

if np.all(c==0):
    ans = True
else:
    ans = False
    
if ans:
    print("Yes")
else:
    print("No")
