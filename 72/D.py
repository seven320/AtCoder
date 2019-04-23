# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


N = int(input())
p = [int(i) for i in input().split()]

ans = 0
f = False
for i in range(N):
    # print(p)
    if i+1==p[i]:
        if i == N-1:
            ans += 1
        else:
            p[i],p[i+1] = p[i+1],p[i]
            ans += 1


print(ans)
