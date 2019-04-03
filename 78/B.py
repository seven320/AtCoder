# encoding:utf-8
import copy
import numpy as np
import random


X,Y,Z = map(int, input().split())

ans = 0

for i in range(1,10**5):
    len = i*Y+(i+1)*Z
    if len > X:
        ans = i-1
        break

print(ans)
