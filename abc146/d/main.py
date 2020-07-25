#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
ab = []
graph = [[] for i in range(N)]
for i in range(N - 1):
    a, b = LI()
    a -= 1
    b -= 1
    ab.append((a,b))
    graph[a].append(b)
    graph[b].append(a)

p = -1
color = 0
max_colors = 0
def bfs(node, p, p_color):
    color = 0
    for new_node in graph[node]:
        if new_node == p: continue
        else:
            color += 1
            if color == p_color:
                color += 1  
            return bfs(new_node, node, color)