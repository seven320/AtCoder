# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


n = int(input())
a = [int(i) for i in input().split()]

b = [0 for i in range(n+1)]
half = n//2
for i in range(n):
    if (i+1)%2==0:
        b[half+(i//2)+1] = a[i]
    else:
        b[half-(i//2)] = a[i]

b.remove(0)
if n%2==0:
    b.reverse()

for i in range(n):
    print(b[i],end=" ")
print("")
