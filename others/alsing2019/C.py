#encoding:utf-8

import numpy as np
import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
S = []
for i in range(H):
    s = list(input())
    S.append(s)


def count_answer(x,y,num_b,num_w):
    # print(used)

    if S[x][y] == "#":
        num_b += 1
    else:
        num_w += 1
    used[x][y] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # print("x,y:",x,y)
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        # print(next_x,next_y)
        if next_x == -1 or next_y == -1 or next_x >= H or next_y >= W:
            pass
        elif used[next_x,next_y] == 1:
            pass
        elif S[next_x][next_y] != S[x][y]:
            num_b,num_w = count_answer(next_x,next_y,num_b,num_w)
    return num_b,num_w

answer = 0
used = np.zeros((H,W))
for i in range(H):
    for j in range(W):
        if used[i][j] == 1:
            continue
        num_b = 0
        num_w = 0
        if S[i][j] == "#":
            num_b,num_w  = count_answer(i,j,num_b,num_w)
            answer += num_b*num_w
print(answer)
