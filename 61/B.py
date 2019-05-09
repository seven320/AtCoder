# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N,M = map(int,input().split())
loads = [[0 for i in range(N)]for j in range(N)]
for i in range(M):
    load = [int(i) for i in input().split()]
    loads[load[0]-1][load[1]-1] += 1
    loads[load[1]-1][load[0]-1] += 1

for i in range(N):
    print(sum(loads[i]))
