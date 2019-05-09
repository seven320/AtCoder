# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N = int(input())
s = []
for i in range(N):
    s.append(int(input()))

ans = sum(s)
s.sort()
if ans % 10 == 0:
    for i in range(N):
        if s[i] % 10 != 0:
            ans -= s[i]
            break
if ans % 10 == 0:
    ans = 0
print(ans)
