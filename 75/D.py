# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

import itertools

N,K = map(int,input().split())
positions = []

for i in range(N):
    x,y = map(int,input().split())
    positions.append([x,y])

positions.sort()

def check(x_min,x_max,y_min,y_max):
    cnt = 0
    for i in range(N):
        x,y = positions[i]
        if x_min <= x <= x_max:
            if y_min <= y <= y_max:
                cnt += 1
                if cnt == K:
                    return True
        elif x>x_max:
            break

    return False


ans = 10**40
for i in range(2,4+1):
    edges =itertools.combinations(positions,i)

    for edge in edges:
        # x_min = 10**10
        # x_max = -10**10
        # y_min = 10**10
        # y_max = -10**10

        xs = sorted(x for x, y in edge)
        ys = sorted(y for x, y in edge)
        x_min, x_max = xs[0], xs[-1]
        y_min, y_max = ys[0], ys[-1]

        # for j in range(i):
            # x,y = edge[j]

            # y_min = min(y_min,y)
            # y_max = max(y_max,y)
            # if j==0:
            #     x_min = x
            # elif j==i-1:
            #     x_max = x

        area = (x_max-x_min)*(y_max-y_min)
        if area < ans:
            if check(x_min,x_max,y_min,y_max):
                ans = area

print(ans)
