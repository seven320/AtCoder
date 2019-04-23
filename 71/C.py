# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


N = int(input())
A = [int(i) for i in input().split()]

A.sort()
len_dic = {}
for a in A:
    if a in len_dic.keys():
        len_dic[a] += 1

    else:
        len_dic[a] = 1

ans = [0,0]
for k, v in sorted(len_dic.items(),key=lambda x:-x[0]):
    if v >= 4 and ans[0] == 0:
        ans = [k,k]
    elif v >= 2:
        if ans[0]==0:
            ans[0] = k
        elif ans[1] == 0:
            ans[1] = k

print(ans[0]*ans[1])
