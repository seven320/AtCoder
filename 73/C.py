# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

N = int(input())

A = []
for i in range(N):
    A.append(int(input()))


paper = {}
for i in range(N):
    if A[i] in paper.keys():
        paper[A[i]] += 1
    else:
        paper[A[i]] = 1

cnt = 0
for key in paper.keys():
    if paper[key] %2 == 0:
        pass
    else:
        cnt += 1


print(cnt)
