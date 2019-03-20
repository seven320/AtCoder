# encoding:utf-8
import copy
import numpy as np
import random


n = int(input())
n_list = list(str(n))

x = 0
for digit in n_list:
    x += int(digit)

if n%x==0:
    print("Yes")
else:

    print("No")
