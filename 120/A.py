# encoding:utf-8
import copy
import numpy as np
import random
import copy


a,b,c = map(int,input().split())

ans = 0
if a*c <= b:
    ans = c
else:
    ans = b//a

print(ans)
