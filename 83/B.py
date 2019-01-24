# encoding:utf-8

import numpy as np
import random

N,A,B = map(int,input().split())

answer = 0
for i in range(N+1):
    n = list(str(i))
    sum = 0
    for j in range(len(n)):
        sum += int(n[j])
    if A <= sum <= B:
        answer += i

print(answer)
