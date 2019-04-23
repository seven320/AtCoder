# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


N = int(input())
S = str(input())
K = int(input())


ans = ""

for i in range(N):
    if S[K-1] == S[i]:
        ans += S[K-1]
    else:
        ans += "*"

print(ans)
