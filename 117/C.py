# encoding:utf-8

import copy
import numpy as np
import random
# import headpq

n,m = map(int,input().split())

x = [int(i) for i in input().split()]

x_sorted = sorted(x)
dif_list = []
for i in range(m-1):
    dif_list.append(x_sorted[i+1]-x_sorted[i])

dif_list = sorted(dif_list)
answer = 0
for i in range((m-1)-(n-1)):
    answer += dif_list[i]

print(answer)
