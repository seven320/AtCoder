# encoding:utf-8
import copy
import numpy as np
import random


n,k = map(int,input().split())
a = [int(i) for i in input().split()]

count_dic = {}

for i in range(len(a)):
    if a[i] in count_dic.keys():
        count_dic[a[i]] += 1
    else:
        count_dic[a[i]] = 1
# print(type(count_dic[1]))

# print(count_dic)
count_list = sorted(count_dic.items(),key=lambda x: x[1],reverse=True)

ans = 0
# print(len(count_list))
while len(count_list)>k:
    # print(count_list)
    delte_tuple = count_list[-1]
    add_tuple = count_list[0]
    count_list[0] = tuple([add_tuple[0],add_tuple[1]+delte_tuple[1]])
    ans += delte_tuple[1]
    del count_list[-1]

print(ans)
