# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    if V[i] > C[i]:
        ans += V[i]-C[i]

print(ans)
