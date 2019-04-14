# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


N = int(input())
H = [int(i) for i in input().split()]


ans = 0
for i in range(N):
    base = H[i]
    check = True
    for j in range(N):
        if i<=j:
            pass
        else:
            if H[i]>=H[j]:
                pass
            else:
                check = False
                break
    if check:
        ans += 1

print(ans)
