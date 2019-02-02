# encoding:utf-8

import copy
import numpy as np
import random

N = int(input())
n = N
C = []
S = []
F = []
for i in range(n-1):
    c,s,f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

answer = []
for i in range(n-1):
    to_goal = C[i] + S[i]
    for j in range(i+1,n-1):
        if to_goal >= S[j]:
            if to_goal % F[j] == 0:
                to_goal += C[j]
            else:
                to_goal = ((to_goal//F[j])+1)*F[j]+C[j]
        elif to_goal < S[j]:
            to_goal = S[j]+C[j]

    answer.append(to_goal)


answer.append(0)
for i in range(len(answer)):
    print(answer[i])
