# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


N,M = map(int,input().split())
a = []
for i in range(M):
    x,y = map(int,input().split())
    a.append([x,y])

ans = False
routes_s = []
routes_g = []

for ai in range(len(a)):
    if 1 in a[ai]:
        inx = a[ai].index(1)
        routes_s.append(a[ai][inx-1])
    if N in a[ai]:
        inx = a[ai].index(N)
        routes_g.append(a[ai][inx-1])

# print(routes)
if 1 in routes_g or N in routes_s:
    print("POSSIBLE")
    exit()

s_reach = list(set(routes_s))
g_reach = list(set(routes_g))
sg_reach = list(set(g_reach+s_reach))

if len(s_reach)+len(g_reach) != len(sg_reach):
    print("POSSIBLE")
    exit()

print("IMPOSSIBLE")
