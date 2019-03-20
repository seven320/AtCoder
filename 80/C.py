# encoding:utf-8
import copy
import numpy as np
import random

n = int(input())
F = []
for i in range(n):
    f = [int(i) for i in input().split()]
    F.append(f)

P = []
for i in range(n):
    P.append([int(i) for i in input().split()])

F = np.array(F)
P = np.array(P)


def cal_val(shop_num,open_time):
    same_time = int(np.dot(F[shop_num],open_time.T))
    return P[shop_num,same_time]

values = []
ans = -10**10
for i in range(1,2**10):
    open_time = np.zeros([10])
    for j in range(10):
        if i%2==1:
            open_time[j] = 1
        i = i//2
    value = 0
    for shop_num in range(n):
        value += cal_val(shop_num,open_time)

    ans = max(ans,value)
