# encoding:utf-8
import copy
import numpy as np
import random

n = int(input())
x = [int(i) for i in input().split()]

x_sorted = sorted(x)

middle = n//2
middle_num = x_sorted[middle]
for i in range(n):
    if x[i] < middle_num:
        print(x_sorted[middle])
    else:
        print(x_sorted[middle-1])
