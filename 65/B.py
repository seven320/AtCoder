# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N = int(input())
a = [0 for i in range(N)]
for i in range(N):
    a[i] = int(input())

cnt = 0
ans = -1
position = 1
for i in range(N):
    position = a[position-1]
    cnt += 1
    if position == 2:
        ans = cnt
        break

print(ans)
