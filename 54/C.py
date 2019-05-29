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
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    tree[a] += [b]
    tree[b] += [a]

# print(tree)
def dfs(node,p,passed):
    # print(node,passed)
    if len(passed) == N:
        return 1
    cnt = 0
    for new_node in tree[node]:
        if new_node == p:
            continue
        if not new_node in passed:
            passed2 = copy.deepcopy(passed)
            passed2 += [new_node]
            cnt += dfs(new_node,node,passed2)
    return cnt

ans = dfs(0,-1,[0])
print(ans)
