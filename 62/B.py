# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

H,W = map(int,input().split())
a = []
for i in range(H):
    a.append(str(input()))

# print(a)
print("#"*(W+2))
for i in range(H):
    print("#"+a[i]+"#")
print("#"*(W+2))
