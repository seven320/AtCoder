# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,M = map(int,input().split())
start = [0 for i in range(N)]
for i in range(N):
    start[i] = [int(i) for i in input().split()]

goal = [[] for i in range(M)]
for i in range(M):
    goal[i] = [int(i) for i in input().split()]

# print(start,goal)
ans = [0 for i in range(N)]
for i in range(N):
    tmp = mod
    for j in range(M):
        if tmp > abs(start[i][0]-goal[j][0])+abs(start[i][1]-goal[j][1]):
            ans[i] = j+1
            tmp = abs(start[i][0]-goal[j][0])+abs(start[i][1]-goal[j][1])
for i in range(N):
    print(ans[i])
