# encoding:utf-8
import copy
import numpy as np
import random
import time
import bisect

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

A.sort()
B.sort()
C.sort()

sum = 0

for i in range(N):
    a = bisect.bisect_left(A,B[i])

    c = N-bisect.bisect_right(C,B[i])
    # print(a,c)

    sum += a*c

print(sum)
