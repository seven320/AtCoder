# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

N = int(input())
A = [int(i) for i in input().split()]

A.sort()
cnt_mi = 0
if A[0] >= 0:
    ans = sum(A)
    print(ans)
    exit()

for i in range(N):
    if A[i] < 0:
        cnt_mi += 1
    A[i] = abs(A[i])

if cnt_mi%2 == 0:
    ans = sum(A)
    print(ans)
    exit()

A.sort()

ans = sum(A)-2*A[0]
print(ans)
