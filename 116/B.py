# encoding:utf-8
import copy
import numpy as np
import random

s = int(input())


def func(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

a = [s]
tmp = s
for i in range(1,10**6):
    tmp = func(tmp)
    if tmp in a:
        print(i+1)
        exit()
    else:
        a.append(tmp)
