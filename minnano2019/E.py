# encoding:utf-8

import copy
import numpy as np
import random
import itertools

n,m = map(int,input().split())

a =[]
for i in range(n):
    a_tem = [int(i) for i in input().split()]
    a.append(a_tem)

a = np.array(a)
print(a)
print(a==1)
