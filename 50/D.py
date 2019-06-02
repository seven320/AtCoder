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

ans = 1
for i in range(60):
    if 2 ** i > N:
        skip = i-1
        break
    else:
        ans += 1
        pass


for i in range(1,skip):
    ans += i*2**i

# print(ans,skip)
for i in range(2**skip,N+1):
    ans += int(2**(skip-1))

print(ans)
