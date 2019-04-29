# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import queue

N = int(input())

ways = {}
for i in range(1,N+1):
    ways[i] = []
for i in range(N-1):
    a,b = map(int,input().split())
    ways[a] += [b]
    ways[b] += [a]

used = [0 for i in range(N+1)]

print(ways)
# fenec

queue = queue.Queue()
queue.put(1)
cnt = 1
while queue.qsize() != 0:
    now = queue.get()
    if used[now] == 0:
        for j in range(len(ways[now])):
            queue.put(ways[now][j])
        used[now] = cnt
    else:
        pass

print(used)


"""
1
2 4 3
7 6
5
"""
