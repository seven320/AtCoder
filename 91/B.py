# encoding:utf-8

import numpy as np
import random

n = int(input())
s = []
t = []
for i in range(n):
    s_tem = str(input())
    s.append(s_tem)

m = int(input())
for i in range(m):
    t_tem = str(input())
    t.append(t_tem)

count_dic = {}

for name in s:
    if name in count_dic.keys():
        count_dic[name] += 1
    else:
        count_dic[name] = 1
for name in t:
    if name in count_dic.keys():
        count_dic[name] -= 1
    else:
        count_dic[name] = -1



sorted_count_dic = sorted(count_dic.items(),key=lambda x:x[1],reverse = True)
answer = max(sorted_count_dic[0][1], 0)
print(answer)
