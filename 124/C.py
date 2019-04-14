# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

S = str(input())

ans_S = [str(0) for i in range(len(S))]
ans_1 = 0
for i in range(len(S)):
    if i%2==0:
        ans_S[i] = str(1)

    if ans_S[i]!=S[i]:
        ans_1 += 1

ans_2 = 0
ans_S = [str(0) for i in range(len(S))]
for i in range(len(S)):
    if i%2==1:
        ans_S[i] = str(1)

    if ans_S[i]!=S[i]:
        ans_2 += 1

ans = min(ans_1,ans_2)
print(ans)
