# encoding:utf-8

import numpy as np
import random
import copy

def select_ok(r_list,b_position):
    pass_list = []
    for i in range(len(r_list)):
        if r_list[i][0] < b_position[0] and r_list[i][1] < b_position[1]:
            pass_list.append(r_list[i])

    return pass_list



n = int(input())
r = []
b = []

for i in range(n):
    position = list(map(int, input().split()))
    r.append(position)

for i in range(n):
    position = list(map(int, input().split()))
    b.append(position)

b_sorted = sorted(b,key=lambda x:x[0])
count = 0
for i in range(n):
    pairs = select_ok(r,b_sorted[i])
    if len(pairs) > 0:
        sorted_pairs = sorted(pairs,key=lambda x:x[1],reverse=True)
        # print(sorted_pairs)
        count += 1
        r.remove(sorted_pairs[0])

print(count)

# print(answer)
