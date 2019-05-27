# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N = int(input())
graph = [set() for i in range(N+1)]

for i in range(N-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    w = w % 2
    graph[u].add((v,w))
    graph[v].add((u,w))


res = [None for i in range(N+1)]

# v は今見ている頂点，p はｖの親
def dfs(node,p,color): # Depth First Serch
    res[node] = color
    for new_node,w in graph[node]:
        if new_node == p:
            pass
        else:
            if w == 1:dfs(new_node,node,1-color)
            else:dfs(new_node,node,color)
#tree 探索　
# vは頂点，ｐは親
dfs(0,-1,0)

for i in range(N):
    print(res[i])
