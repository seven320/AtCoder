# encoding:utf-8

import copy
import numpy as np
import random

n = int(input())

p = []
for i in range(n):
    p.append(int(input()))

answer = sum(p)-max(p)//2

print(answer)
