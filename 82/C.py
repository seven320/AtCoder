# encoding:utf-8
import copy
import numpy as np
import random
n = int(input())

A = [int(i) for i in input().split()]


count_dic = {}
for a in A:
    if a in count_dic:
        count_dic[a] += 1
    else:
        count_dic[a] = 1

ans = 0

for key in count_dic.keys():
    if count_dic[key] == key:
        pass
    elif count_dic[key]<key:
        ans += count_dic[key]
    else:
        ans += count_dic[key]-key
        count_dic[key] = key


print(ans)
