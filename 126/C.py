# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,K = map(int,input().split())

pro = 0
for i in range(1,N+1):
    cnt = 0
    points = i
    while points < K:
        points *= 2
        cnt += 1
    # print(cnt)
    pro += (1/2)**cnt/N

print(pro)
