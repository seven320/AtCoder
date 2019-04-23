# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

H,W = map(int,input().split())

# a = [[0 for i in range(W)] for j in range(H)]
a = []
for i in range(H):
    a.append([int(j) for j in input().split()])


ans = []
# print(a)
for hi in range(H):
    for wi in range(W):
        if a[hi][wi] % 2 == 1 and wi < W-1:
            #move
            ans.append([hi,wi,hi,wi+1])
            a[hi][wi] -= 1
            a[hi][wi+1] += 1

for hi in range(H):
    if a[hi][-1]%2 == 1 and hi < H-1:
        ans.append([hi,W-1,hi+1,W-1])
        a[hi][-1] -= 1
        a[hi+1][-1] += 1

print(len(ans))
for i in range(len(ans)):
    x,y,dx,dy = ans[i]
    print(x+1,y+1,dx+1,dy+1)

# print(a)
