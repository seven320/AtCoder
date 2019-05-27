# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


N,M = map(int,input().split())
tree = [[] for i in range(N)]
for i in range(M):
    X,Y,Z = map(int,input().split())
    X -= 1
    Y -= 1
    tree[X] += [Y]
    tree[Y] += [X]

# print(tree)
used = [0 for i in range(N)]

def dfs(node,p):
    used[node] = 1
    # print(tree[node])
    for new in tree[node]:
        if new == p or used[new] == 1:continue
        dfs(new,node)

cnt = 0
while sum(used) < len(used):
    for i in range(N):
        if used[i] == 0:
            dfs(i,-1)
            cnt += 1

ans = cnt
print(ans)
