# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


H,W = map(int, input().split())
N = int(input())
a = [int(i) for i in input().split()]

color_count = {}
for i in range(N):
    color_count[i+1] = a[i]

color_count = dict(sorted(color_count.items(),key=lambda x:-x[1]))


mas = [[0 for i in range(W)] for j in range(H)]
colors = list(color_count.keys())

color = colors[0]
color_i = 0
color_cnt = color_count[color]
cnt = 0

for h_i in range(H):
    if h_i%2==0:
        for w_i in range(W):
            mas[h_i][w_i] = color
            cnt += 1
            if h_i == H - 1 and w_i == W-1:
                break
            if cnt == color_cnt:
                color_i += 1
                color = colors[color_i]
                cnt = 0
                color_cnt = color_count[color]
    else:
        for w_i in reversed(range(W)):
            mas[h_i][w_i] = color
            cnt += 1
            if h_i == H - 1 and w_i == 0:
                break
            if cnt == color_cnt:
                color_i += 1
                color = colors[color_i]
                cnt = 0
                color_cnt = color_count[color]

# print(mas)
for h_i in range(H):
    for w_i in range(W):
        print(mas[h_i][w_i],end=" ")
    print()
