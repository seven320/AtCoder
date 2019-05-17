# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N = int(input())
s = round(math.sqrt(N))

ans = 0
for i in range(1,s+1):
    if N % i == 0:
        m = N//i-1
        # print(m)

        if m > 0 and i < m:
            ans += m

print(ans)
