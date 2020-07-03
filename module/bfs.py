# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()


root = 2 # start位置となるrootを選択
queue = collections.deque()

# 初期化　startからのstep数を保存する
visited = [-1 for i in range(N + 1)] 

queue.append(root)
visited[root] = 0

while len(queue) > 0:
    node = queue.popleft()
    cnt = visited[node]
    for n_node in G[node]:
        if visited[n_node] == -1:
            visited[n_node] = cnt + 1
            queue.append(n_node)

print(visited)