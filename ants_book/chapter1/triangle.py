# encoding:utf-8

import copy
import numpy as np
import random
import itertools

n = int(input())
a = [int(i) for i in input().split()]
answer = 0
for combination in itertools.combinations(a,3):
    sum_com = sum(combination)
    count = 0
    for i in range(3):
        if sum_com - combination[i] > combination[i]:
            count += 1
        else:
            break

    if count == 3:
        answer = max(sum_com,answer)

print(answer)
