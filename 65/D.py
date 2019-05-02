# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N = int(input())
cities = [0 for i in range(N)]
for i in range(N):
    cities[i] = [int(i) for i in input().split()]
max_x = -1
max_y = -1
min_x = 10**9
min_y = 10**9

for i in range(N):
    x,y = cities[i]
    max_x = max(max_x,x)
    min_x = min(min_x,x)
    max_y = max(max_y,y)
    min_y = min(min_y,y)

print(min((max_x-min_x),(max_y-min_y)))    
