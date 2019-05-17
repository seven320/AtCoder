# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

s = [str(i) for i in input().split()]

ans = ""
for i in range(3):
    ans += s[i][0]

print(ans.upper())
