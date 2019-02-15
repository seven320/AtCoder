# encoding:utf-8

import copy
import numpy as np
import random
import itertools

l = int(input())
n = int(input())

x = [int(i) for i in input().split()]


min_time = 0
max_time = 0
for i in range(n):
    if x[i] > l/2:
        min_time = max(l-x[i],min_time)
        max_time = max(x[i],max_time)

    else:
        min_time = max(min_time,x[i])
        max_time = max(max_time,l-x[i])

print(min_time)
print(max_time)
