# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

N = int(input())
a = [int(i) for i in input().split()]

a.sort()

counts = {}
for i in range(N):
    if a[i] in counts.keys():
        counts[a[i]] += 1
    else:
        counts[a[i]] = 1

counts_list = []
tmp = 0
for num in range(max(a)+1):
    try:
        tmp += counts[num]
        # counts_list.append(tmp)
    except:
        pass

    counts_list.append(tmp)

ans = 0
for i in range(len(counts_list)-3):
    ans = max(ans,counts_list[i+3]-counts_list[i])
    # print(ans)

#例外処理
if len(counts_list) <= 3:
    ans = max(ans,max(counts_list))

print(ans)
