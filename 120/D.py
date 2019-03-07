# encoding:utf-8
import copy
import numpy as np
import random


n,m = map(int,input().split())
bridges = []
for i in range(m):
    a,b = map(int,input().split())
    bridges.append([a,b])


ans = [0 for i in range(m)]
uncon = n*(n-1)//2

group_count = [1 for i in range(n+1)]

islands = {}
for island in range(1,n+1):
    islands[island] = island

for i in reversed(range(m)):
    ans[i] = uncon
    a,b = bridges[i]
    # print(a,b)
    # print(islands)
    pre_group_a = islands[a]
    pre_group_b = islands[b]
    uncon = max(0,uncon-group_count[pre_group_a]*group_count[pre_group_b])
    new_group = min(pre_group_a,pre_group_b)

    keys = [k for k,v in islands.items() if v==pre_group_a]
    for key in keys:
        islands[key] = new_group
    keys = [k for k,v in islands.items() if v==pre_group_b]
    for key in keys:
        islands[key] = new_group

    group_count[new_group] += group_count[max(pre_group_a,pre_group_b)]

for i in range(m):
    print(ans[i])
