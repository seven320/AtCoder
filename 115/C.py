# encoding:utf-8

import copy
import numpy as np
import random

n,k = map(int,input().split())

h = []
for i in range(n):
    h.append(int(input()))

tree_count = {}
for i in range(n):
    if h[i] in tree_count.keys():
        tree_count[h[i]] += 1
    else:
        tree_count[h[i]] = 1

tree_count = sorted(tree_count,key=tree_count.item() x:x[1])
print(tree_count)
# for key in tree_count.keys():
#     count = tree_count[key]
