# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
B = [0 for i in range(N+1)]
B[0] = -1
for i in range(N-1):
    B[i+1] = int(input()) - 1


crew = {}
for i in range(N):
    crew[i] = []
# print(crew,B)
for i in range(1,N):
    crew[B[i]].append(i)



salary = [0 for i in range(N)]
def dfs(node,p):
    if len(crew[node]) == 0:
        return 1
    else:
        salaries = []
        for new_node in crew[node]:
            if new_node == p:
                continue
            else:
                salaries.append(dfs(new_node, node))

        return max(salaries) + min(salaries) + 1
print(dfs(0,-1))
