# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

O = str(input())
E = str(input())

ans = ""
for i in range(len(E)):
    ans += O[i]
    ans += E[i]

if len(O)-len(E) == 1:
    ans += O[-1]

print(ans)
