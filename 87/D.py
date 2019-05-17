# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,M = map(int,input().split())
L,R,D = [0 for i in range(M)],[0 for i in range(M)],[0 for i in range(M)]

for i in range(M):
    L[i],R[i],D[i] = map(int,input().split())

dist = [[None for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    l,r,d = L[i],R[i],D[i]
    if dist[l][r] == None:
        dist[l][r] = d
        dist[r][l] = -d
    else:
        dist
