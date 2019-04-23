# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

A,B,C,D = map(int,input().split())

cnt = 0
for i in range(101):
    if A<i<=B and C< i <= D:
        cnt += 1

print(cnt)
