# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
A = [int(i) for i in input().split()]

A.sort()
if N == 2:
    print(A[1]-A[0])
    print(A[1],A[0])
    exit()

A.reverse()
max_num = A[0]
min_num = A[-1]
exchanges = [() for i in range(N-1)]
for i in range(1,N-1):
    if A[i] < 0:
        exchanges[i-1] = (max_num,A[i])
        max_num = max_num - A[i]
    else:
        exchanges[i-1] = (min_num,A[i])
        min_num = min_num - A[i]

exchanges[-1] = (max_num,min_num)
ans = max_num-min_num
print(ans)
for i in range(N-1):
    a,b = exchanges[i]
    print(a,b)
