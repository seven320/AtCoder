# encoding:utf-8

import copy
import numpy as np
import random

n,k = map(int,input().split())

h = []
for i in range(n):
    h.append(int(input()))

h.sort()
# print(h)
max_tree = []
min_tree = []
ans = 10**9
for i in range(n-k+1):
    ans = min(h[i+k-1]-h[i],ans)

print(ans)
