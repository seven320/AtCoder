# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9
# sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N,M,T,K = LI()
ABCD = [[] for i in range(M)]
for i in range(M):
    a,b,c,d = LI()
    a -= 1
    b -= 1
    ABCD[i] = [a,b,c,d]

graphs = [[] for i in range(N)]


for m_i in range(M):
    a,b,c,d = ABCD[m_i]
    graphs[a].append([b,m_i])
    graphs[b].append([a,m_i])


def time_pass(t,c,d):
    if T - t > 0:

        max_dense = 0
        for i in range(t,t+c+1):
            max_dense = max(max_dense,d-abs(T-i))
        if max_dense > K:
            j = -K-d-T
            return j+c
        else:
            print("hog")
            return t+c
    else:
        i = -K-D-T
        return i+c

DP = [mod for i in range(N)]
stuck = [0]
DP[0] = 0

while len(stuck) != 0:
    print(DP)
    node = stuck.pop()
    for next_nodes,road_i in graphs[node]:
        a,b,c,d = ABCD[road_i]
        next_time = time_pass(DP[node],c,d)
        print(next_time)
        if DP[next_nodes] > next_time:
            DP[next_nodes] = next_time
            stuck.append(next_nodes)

if DP[-1] == mod:
    print(-1)
else:
    print(DP[-1])

# v は今見ている頂点，p はｖの親
# def dfs(node,p,time): # Depth First Serch
#     # 終了条件を書く
#     # if graph[node] == xx:
#     # return xxx
#     if node == N-1:
#         return time
#
#     for new_node,road_i in graphs[node]:
#
#         if new_node == p:continue
#         else:
#             a,b,c,d = ABCD[road_i]
#             passtime = time_pass(time,c,d)
#             return dfs(new_node,node,passtime)#深掘りする条件を書く
# #tree 探索　
#
# # node:0から　p:最初はなしなので-1
#
# print(dfs(0,-1,0))
