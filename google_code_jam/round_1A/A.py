# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


T = int(input())
gala = []
for t in range(T):
    r,c = map(int,input().split())
    gala.append([r,c])


def solve(pair):
    r,c = pair
    space = []
    for i in range(r):
        for j in range(c):
            space.append([i,j])

    way = []
    pos = [0,0]
    space.remove(pos)
    way.append(pos)
    space_0 = copy.deepcopy(space)
    result = True
    for i in range(r*c*100000):
        space = copy.deepcopy(space_0)
        way = []
        random.shuffle(space)
        # print(space)
        x,y = pos
        while len(space) > 0:
            nx,ny = space.pop()
            if x==nx or y==ny or x+y==nx+ny or x-y==nx-ny:
                result = False
                break
            else:
                way.append([nx,ny])
                x,y = nx,ny
                # print(way)

        if result:
            print("hoge")
            break

    return way,result



# print(gala)
for i in range(T):
    way,result = solve(gala[t])
    if result:
        print("Case #"+str(i+1)+": POSSIBLE")
        for time_way in range(len(way)):
            i,j = way[time_way]
            print(i,j)
    else:
        print("Case #"+str(i+1)+": IMPOSSIBLE")
