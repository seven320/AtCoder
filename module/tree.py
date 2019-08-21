# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

# v は今見ている頂点，p はｖの親
def dfs(node,p): # Depth First Serch
    # 終了条件を書く
    # if graph[node] == xx:
    # return xxx

    for new_node,w in graph[node]:
        if new_node == p:continue
        else:
            return dfs(new_node,node)#深掘りする条件を書く
#tree 探索　

# node:0から　p:最初はなしなので-1

dfs(0,-1)
