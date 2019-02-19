# encoding:utf-8

import copy
import numpy as np
import random

s = list(str(input()))
t = list(str(input()))

s.sort()
t.sort(reverse=True)
# print(s,t)

ans = False
min_str = min(len(s),len(t))
for i in range(min_str):
    if s[i]==t[i]:
        if min_str-1 == i and len(t)>len(s):
            ans = True
    elif s[i]>t[i]:
        ans = False
        break
    else:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
