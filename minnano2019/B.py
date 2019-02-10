# encoding:utf-8

import copy
import numpy as np
import random

a = []
b = []

for i in range(3):
    a_now,b_now = map(int, input().split())
    a.append(a_now)
    b.append(b_now)

town_dic = {1:0,2:0,3:0,4:0}

for i in range(3):
    town_dic[a[i]] += 1
    town_dic[b[i]] += 1

answer = "YES"
for i in range(4):
    if town_dic[i+1] == 3:
        answer = "NO"


print(answer)
