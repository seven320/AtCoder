#encoding:utf-8

# encoding:utf-8
import copy
import numpy as np
import random

d,g = map(int, input().split())
P = [0]
C = [0]
for i in range(d):
    p,c = map(int,input().split())
    P.append(p)
    C.append(c)

# j = max(C)
# i = d

problems = sum(P)
dp = [[0 for i in range(problems+1)] for j in range(d+1)]



for i in range(1,d+1):
    for j in range(1,max(P)+1):
        if j < P[i]:
            dp[i][j] = (j)*100*(i)
        elif j==P[i]:
            dp[i][j] = (j)*(i)*100+C[i]
        else:
            pass



dp2 = copy.deepcopy(dp)
for i in range(1,d+1):
    for j in range(1,problems):
        if dp2[i][j] == 0:
            print(dp[i][P[i]])
            dp2[i][j] = max(dp2[i-1][j],dp[i][P[i]]+dp2[i-1][j-P[i]])
        else:
            dp2[i][j] = max(dp[i][j],dp[i-1][j])
print(dp)
print(dp2)

for i in range(problems):
    if dp[-1][i] >= g:
        print(i)
        exit()
