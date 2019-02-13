# encoding:utf-8

import copy
import numpy as np
import random
import time

n,m = map(int,input().split())

lakes = []
for i in range(n):
    lake=list(input())
    lakes.append(lake)
#
# def change2land(i,j,lakes):
#     lakes[i][j] = "."
#     for x_axis in range(-1,2):
#         for y_axis in range(-1,2):
#             if 0<=x_axis+i<n and 0<= y_axis+j < m:
#                 if lakes[x_axis+i][y_axis+j] == "W":
#                     lakes = change2land(x_axis+i,y_axis+j,lakes)
#     return lakes
#
# count = 0
# for i in range(n):
#     for j in range(m):
#         if lakes[i][j] == "W":
#             lakes = change2land(i,j,lakes)
#             count += 1
#
# print(count)


# xの移動分をdx　新しいxの座標をnxとおいているのがわかりやすい


def dfs(x,y):
    lakes[x][y] = "."

    for dx in range(-1,2):
        for dy in range(-1,2):
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and lakes[nx][ny] == "W":
                dfs(nx,ny)

count = 0
for i in range(n):
    for j in range(m):
        if lakes[i][j] =="W":
            dfs(i,j)
            count += 1

print(count)
