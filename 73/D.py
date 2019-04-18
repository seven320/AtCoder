# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math
import itertools

f_inf = float('inf')

N,M,R = map(int,input().split())
nodes = list(map(int,input().split()))
ways = []
for i in range(M):
    a,b,c = map(int,input().split())
    ways.append([a,b,c])

def warshall_floyd(n):
    dp = [[f_inf for i in range(N)] for j in range(N)]
    for i in range(n):
        dp[i][i] = 0
    for way in ways:
        dp[way[0]-1][way[1]-1] = way[2]
        dp[way[1]-1][way[0]-1] = way[2]

    for i in range(N):#頂点数　ノード数
        for j in range(N):#始点
            for k in range(N):#終点
                dp[j][k] = min(dp[j][k],dp[j][i]+dp[i][k])

    return dp


dp = warshall_floyd(N)
routes = list(itertools.permutations(nodes))

ans = f_inf
for route in routes:
#     route = list(print(route))
    tmp = 0
    for i in range(len(route)-1):
        # print(route[i])
        tmp += dp[route[i]-1][route[i+1]-1]
    ans = min(ans,tmp)


print(ans)
