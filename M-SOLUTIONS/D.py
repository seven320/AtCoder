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
ab = [0 for i in range(N-1)]
for i in range(N-1):
    ab[i] = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

c.sort(reverse = True)

tree = {}
for i in range(N):
    tree[i] = []
for i in range(N-1):
    a,b = ab[i]
    a -= 1
    b -= 1
    tree[a] += [b]
    tree[b] += [a]

# print(tree)
idx =  sorted(tree, key=lambda k:len(tree[k]))
idx.reverse()

node = [0 for i in range(N)]


node[idx[0]] = c[0]
id = idx[0]
for next in tree[id]:
    tree[next]







ans = 0
for i in range(N-1):
    a,b = ab[i]
    a -= 1
    b -= 1
    ans += min(node[a],node[b])
print(ans)
for i in range(N):
    print(node[i],end=" ")
print()
