#encoding:utf-8

# encoding:utf-8
import copy
import numpy as np
import random

d,g = map(int, input().split())
P = []
C = []
for i in range(d):
    p,c = map(int,input().split())
    P.append(p)
    C.append(c)

completed = []
for i in range(d):
    score = P[i]*(i+1)*100+C[i]
    completed.append(score)

def to_digital(num):
    dig = [0]*d
    for i in range(d):
        dig[i]=num%2
        num //= 2
    return dig

ans = 10**9
for i in range(2**d):
    digital = to_digital(i)
    score = 0
    count = 0
    for j in range(d):
        if digital[j]:
            score += completed[j]
            count += P[j]

    for j in range(d)[::-1]:
        if digital[j]==0:
            for k in range(P[j]-1):
                if g<=score:
                    break
                else:
                    count += 1
                    score += 100*(j+1)
        if g<=score:
            ans = min(ans,count)

print(ans)
