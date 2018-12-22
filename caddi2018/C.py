#encoding:utf-8

import math
from collections import Counter

N,P = map(int,input().split())

ans = 1
if N == 1:
    ans = P
elif 1 < N < 40:
    for i in range(2,round(P**(1/N))+1):
        if P % i**N == 0:
            ans = i
else:
    pass

print(int(ans))
# print(type(ans))
