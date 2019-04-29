# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

N = int(input())
a = [int(i) for i in input().split()]

sum_a = sum(a)

ans = 10**10
x = 0
for i in range(N-1):
    x += a[i]
    ans = min(ans,abs(sum_a-2*x))

print(ans)
