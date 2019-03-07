# encoding:utf-8
import copy
import numpy as np
import random

n,m,x = map(int,input().split())

a = [int(i) for i in input().split()]



#migi
cost_r = 0
for i in range(x,n):
    if i in a:
        cost_r += 1

cost_l = 0
for i in range(x):
    if i in a:
        cost_l += 1

print(min(cost_l,cost_r))
