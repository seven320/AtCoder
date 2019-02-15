# encoding:utf-8
import copy
import numpy as np
import random

n=int(input())
l=[int(i) for i in input().split()]

l.sort()
ans = 0
while n>1:
    mil1=0
    mil2=1
    for i in range(2,n):
        if l[i] < l[mil1]:
            mil2 = mil1
            mil1 = i
        elif l[i] < l[mil2]:
            mil2 = i

    t = l[mil1]+l[mil2]
    ans += t

    if mil1==n-1:
        swap(mil1,mil2)
    l[mil1] = t
    l[mil2] = l[n-1]
    n-=1

print(ans)
