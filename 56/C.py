# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


X = int(input())
position = 0
cnt = 0
for i in range(1,mod):
    cnt += 1
    position += i
    if position >= abs(X):
        break

print(cnt)
