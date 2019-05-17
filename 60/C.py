# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N,T = map(int,input().split())
t = [int(i) for i in input().split()]
ans = 0
difference = [0 for i in range(N-1)]
for i in range(N-1):
    difference[i] = t[i+1]-t[i]

# print(difference)
for i in range(N-1):
    if difference[i] >= T:
        ans += T
    else:
        ans += difference[i]

ans += T
print(ans)
