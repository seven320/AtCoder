# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N = int(input())
a = [int(i) for i in input().split()]


# part
left = a[:N]

left.sort()

for i in range(N,2*N+1):
    if left[0] < a[i]:
        left[0] = a[i]
        left.sort()

right = a[2*N:]
right.sort()
for i in range(N,2*N):
    print(right)
    if right[-1] > a[i]:
        right[-1] = a[i]
        right.sort()

print(left,right)
ans = sum(left)-sum(right)

print(ans)
