# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N = int(input())
ans = 10
for i in range(1,round(math.sqrt(N))+1):
    if N % i == 0:
        f = max(i,N//i)
        f = len(str(f))
        ans = min(f,ans)
    else:
        pass
print(ans)
