# encoding:utf-8

import copy
import numpy as np
import random

n = int(input())

l = [int(i) for i in input().split()]

sum_all = 0
for i in range(n):
    sum_all += l[i]

answer = "Yes"
for i in range(n):
    if l[i] < sum_all-l[i]:
        pass
    else:
        answer = "No"

print(answer)
