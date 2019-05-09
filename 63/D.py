# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N,A,B = map(int,input().split())
h = []
for i in range(N):
    h.append(int(input()))

h.sort()
cnt = math.ceil(h[-1]/A)

(h[-1] - cnt * A)
print(cnt)
