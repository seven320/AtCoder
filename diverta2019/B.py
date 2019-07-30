# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
xy = [[] for i in range(N)]
for i in range(N):
    xy[i] = [int(i) for i in input().split()]

xy = np.array(xy)
count_dic = {}
for i in range(N):
    for j in range(i+1,N):
        diff = xy[i] - xy[j]
        p,q = diff
        if p == 0 and q == 0:
            pass
        else:
            k = (p,q)
            if k in count_dic:
                count_dic[k] += 1
            else:
                count_dic[k] = 1
            k = (-p,-q)
            if k in count_dic:
                count_dic[k] += 1
            else:
                count_dic[k] = 1


"""
            p = int(p)
            q = int(q)
            pq = str(p)+str(q)
            pq2 = str(-p)+str(-q)
            if pq in count_dic:
                count_dic[pq] += 1
            else:
                count_dic[pq] = 1
            if pq2 in count_dic:
                count_dic[pq2] += 1
            else:
                count_dic[pq2] = 1

"""
# print(count_dic)
ans = 1
for k,v in sorted(count_dic.items(), key = lambda x:-x[1]):
    ans = N - v
    break
print(max(1,ans))
