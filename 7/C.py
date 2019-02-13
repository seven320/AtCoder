# encoding:utf-8

import copy
import numpy as np
import random
import sys
import time
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1

maze = []
reached = np.zeros((n,m))
for i in range(n):
    maze.append(list(str(input())))

for i in range(n):
    for j in range(m):
        if maze[i][j] == "S":
            sx,sy = i,j

options = [[-1,0],[1,0],[0,-1],[0,1]]

def move(x,y,count):
    print(reached)
    print(x,y)
    time.sleep(1)
    count += 1
    for option in options:
        nx = x+option[0]
        ny = y+option[1]
        if 0<=nx<n and 0<=ny<m:
            if nx == gx and ny == gy:
                print(count)
                exit()
            elif maze[nx][ny] == "." and reached[nx,ny]==0:
                reached[nx,ny] = count
                move(nx,ny,count)


move(sx,sy,0)
