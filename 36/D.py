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
ab = [[] for i in range(N)]
for i in range(N - 1):
    a,b = LI()
    a -= 1
    b -= 1
    ab[i] = [a,b]

bridges = {}
for i in range(N):
    bridges[i] = []
for i in range(N - 1):
    a,b = ab[i]
    bridges[a].append(b)
    bridges[b].append(a)

# print(bridges)

# color : 0:white, 1:black
reserched = [[-1 for i in range(2)]for j in range(N)]

def dfs(node, p, color):
    # print(node, p)
    # print("b",bridges[node])
    if len(bridges[node]) == 1 and bridges[node][0] == p:
        if color:
            cnt = 1
        else:
            cnt = 2
        reserched[node][color] = cnt
        return cnt
    if reserched[node][color] == -1:
        cnt = 1
        for new_node in bridges[node]:
            if new_node == p:pass
            else:
                if color:
                    cnt *= dfs(new_node, node, 0)
                else:
                    cnt *= (dfs(new_node, node, 1) + dfs(new_node, node, 1))
        reserched[node][color] = cnt
        return cnt
    else:
        return reserched[node][color]

ans = 0
for color in range(2):
    ans += dfs(0, -1, color)
print(ans)
# print(reserched)
