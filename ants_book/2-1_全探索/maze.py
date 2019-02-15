# encoding:utf-8

import copy
import numpy as np
import random
import queue
# que.put() or que.get()


n,m = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())

sx-=1
sy-=1
gx-=1
gy-=1



field = []
inf = 10**2
visited = [[inf for i in range(m)] for i in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    field.append(list(str(input())))

q = queue.Queue()


# Breadth-First Serch
def bfs(sx,sy):
    field[sx][sy] = "."
    visited[sx][sy] = 0
    q.put([sx,sy])
    while not q.empty():
        x,y = q.get()
        if x==gx and y==gy:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and field[nx][ny]=="." and visited[nx][ny]==inf:
                q.put([nx,ny])
                visited[nx][ny] = visited[x][y] + 1

    return visited[gx][gy]

print(bfs(sx,sy))
