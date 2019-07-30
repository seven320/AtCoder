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
    # res[node] = color
    for new_node,w in graph[node]:
        if new_node == p:continue
        if w == 1:dfs(new_node,node)
        else:dfs(new_node,node)
#tree 探索　

# node:0から　p:最初はなしなので-1

dfs(0,-1)
