# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える

h,w = map(int,input().split())
s = ["."*(w+2)]
for i in range(h):
    s.append("."+str(input())+".")
s.append("."*(w+2))

ans = [[0 for i in range(w)] for i in range(h)]
# print(s)
for i in range(h):
    for j in range(w):
        if s[i+1][j+1]=="#":
            ans[i][j] = "#"
        else:
            count = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    # print(i+dx+1,j+dy+1)
                    if dx==0 and dy==0:
                        pass
                    else:
                        if s[i+dx+1][j+dy+1] == "#":
                            count += 1
            ans[i][j] = str(count)
for i in range(h):
    print("".join(ans[i]))
