# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

R,G,B,N = map(int,input().split())

ans = 0

box = [R,G,B]
box.sort()

flag = False
R,G,B = box[2],box[1],box[0]
for i in range(3000//R+1):
    if flag:
        pass
    else:
        if N-i*R < 0:
            flag = True
            break
        for j in range(3000//G+1):
            if N-i*R-j*G<0:
                break
            if (N-i*R-j*G)%B == 0:
                # print(i*R+j*G)
                # print(i,j,(N-i*R-j*G)//B)
                ans += 1

print(ans)
