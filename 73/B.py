# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


N = int(input())
groups = []
for i in range(N):
    l,r = map(int,input().split())
    groups.append([l,r])

cnt = 0
for i in range(N):
    cnt += groups[i][1]-groups[i][0]+1

print(cnt)
