# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))


N,K = LI()
ab = [0 for i in range(N-1)]
for i in range(N-1):
    ab[i] = LI()

edges = {}
for i in range(N):
    edges[i] = []
count = [0 for i in range(N)]
for i in range(N-1):
    a,b = ab[i]
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def dfs(node,p):
    cnt = 0
    for i,new_node in enumerate(edges[node]):
        if new_node == p:
            continue
        else:
            p_cnt = 2
            if node == 0:
                p_cnt = 1
            count[new_node] = K - p_cnt - cnt
            cnt += 1
            dfs(new_node,node)


count[0] = K
dfs(0,-1)
# print(count)
ans = 1
for i in range(N):
    ans = ans *count[i] % mod

print(ans)
