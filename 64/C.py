# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N = int(input())
a = [int(i) for i in input().split()]


counts = [0 for i in range(8)]
any = 0
for i in range(N):
    if a[i] >= 3200:
        any += 1
    else:
        ind = a[i] // 400
        counts[ind] += 1

# print(counts)

ans_min = max(1,len(counts)-counts.count(0))
if counts.count(0) != 8:
    ans_max = ans_min+any
else:
    ans_max = any
print(ans_min,ans_max)
